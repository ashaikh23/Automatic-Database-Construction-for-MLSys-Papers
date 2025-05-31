import os
from dotenv import load_dotenv
from semantic_scholar import SemanticScholarClient, RateLimitException, ServerException
import csv
import time
import numpy as np

load_dotenv()
key = os.getenv("SEMANTIC_API_KEY") or ""
client = SemanticScholarClient(api_key=key)

def get_ids(titles: list[str]) -> list[str]:
    ids = []
    i = 0

    for title in titles:
        finished = False
        while not finished:
            try:
                data = client.get_paper_by_title(title, fields=['paperId', 'title'])
                print(f"{i+1}: Found {title}")
                ids.append(data['paperId'])
                finished = True
            except RateLimitException:
                print("Rate limit exceeded, sleeping...")
                time.sleep(1)
            except ServerException as err:
                print(err)
                finished = True
        i += 1

    return ids

def get_embeddings(ids: list[str], labels: list[int]) -> list[list[float]]:
    embeddings = []
    no_embed = 0
    server_err = []
    i = 0

    for id, label in zip(ids, labels):
        finished = False
        while not finished:
            try:
                data = client.get_paper_by_id(id, fields=['paperId', 'embedding.specter_v2'])
                emb = data['embedding']
                if emb:
                    embeddings.append(emb['vector'] + [label])
                    print(f"{i+1}: Found embedding for {id}")
                else:
                    print(f"{i+1}: Did not find embedding for {id}")
                    no_embed += 1
                finished = True
            except RateLimitException:
                print("Rate limit exceeded, sleeping...")
                time.sleep(1)
            except ServerException as err:
                print(err)
                server_err.append(id)
                finished = True
        i += 1

    print(f"Embedding: {len(embeddings)}")
    print(f"No Embedding: {no_embed}")
    print(f"Server Errors: {len(server_err)}")
    print(server_err)
    
    return embeddings

embeddings = []

with open("negative_papers.csv") as file:
    csv_file = csv.DictReader(file)
    titles = [line['Title'] for line in csv_file][:5]
    ids = get_ids(titles)
    arr = get_embeddings(ids, [0] * len(ids))
    embeddings.extend(arr)

with open("mlsys_more_labeled.csv") as file:
    csv_file = csv.DictReader(file)
    results = [(line['ID'], line['Is MLSys?']) for line in csv_file]
    ids = [result[0] for result in results]
    labels = [int(result[1] == "Y") for result in results]
    arr = get_embeddings(ids, labels)
    embeddings.extend(arr)

with open("seed.csv") as file:
    csv_file = csv.DictReader(file)
    ids = [line['Paper ID'] for line in csv_file]
    arr = get_embeddings(ids, [1] * len(ids))
    embeddings.extend(arr)

np.save("final_embedding", np.array(embeddings))


# From Negative Papers
# The `Get Paper By Title` did not return these papers for some reasons
#  - Equivariant Flow Matching with Hybrid Probability Transport for 3D Molecule Generation
#  - Zeroth-Order Methods for Nondifferentiable, Nonconvex, and Hierarchical Federated Optimization
#  - Complexity of Derivative-Free Policy Optimization for Structured $\mathcal{H}_\infty$ Control
# which are added below
#
# arr = np.load("final_embedding.npy")
#
# ids = ['6d77d4a044ee4a1eb928a65f722cf218e2fddbfa',
#        '755689b414ca98e442cea99e3631ee9d2d3c253b',
#        '14f3a19c9bbb95d1c1ebb913de913859ad06fc3f']
#
# additional_embeddings = []
# for id in ids:
#     data = client.get_paper_by_id(id, fields=['paperId', 'embedding.specter_v2'])
#     emb = data['embedding']
#     if emb:
#         additional_embeddings.append(emb['vector'] + [0])
#     else:
#         print("no embedding for", id)
#
# arr_add = np.array(additional_embeddings)
# arr_new = np.vstack((arr, arr_add))
# np.save("final_embedding", np.array(arr_new))
#
# Other papers in the CSV but not in Semantic Scholars are:
#  - Q$^2$Chemistry: A quantum computation platform for quantum chemistry
#  - A Statistical Mechanical Approach to Combinatorial Chemistry
#  - Organic chemistry in a CO2 rich early Earth atmosphere
