import requests

AVAILABLE_FIELDS = {
    "paperId",
    "corpusId",
    "externalIds",
    "url",
    "title",
    "abstract",
    "venue",
    "publicationVenue",
    "year",
    "referenceCount",
    "citationCount",
    "influentialCitationCount",
    "isOpenAccess",
    "openAccessPdf",
    "fieldsOfStudy",
    "s2FieldsOfStudy",
    "publicationTypes",
    "publicationDate",
    "journal",
    "citationStyles",
    "authors.authorId",
    "authors.externalIds",
    "authors.url",
    "authors.name",
    "authors.affiliations",
    "authors.homepage",
    "authors.paperCount",
    "authors.citationCount",
    "authors.hIndex",
    "citations.paperId",
    "citations.corpusId",
    "citations.externalIds",
    "citations.url",
    "citations.title",
    "citations.abstract",
    "citations.venue",
    "citations.publicationVenue",
    "citations.year",
    "citations.referenceCount",
    "citations.citationCount",
    "citations.influentialCitationCount",
    "citations.isOpenAccess",
    "citations.openAccessPdf",
    "citations.fieldsOfStudy",
    "citations.s2FieldsOfStudy",
    "citations.publicationTypes",
    "citations.publicationDate",
    "citations.journal",
    "citations.citationStyles",
    "citations.authors",
    "references.paperId",
    "references.corpusId",
    "references.externalIds",
    "references.url",
    "references.title",
    "references.abstract",
    "references.venue",
    "references.publicationVenue",
    "references.year",
    "references.referenceCount",
    "references.citationCount",
    "references.influentialCitationCount",
    "references.isOpenAccess",
    "references.openAccessPdf",
    "references.fieldsOfStudy",
    "references.s2FieldsOfStudy",
    "references.publicationTypes",
    "references.publicationDate",
    "references.journal",
    "references.citationStyles",
    "references.authors",
    "embedding",
    "embedding.specter_v2"
}

AVAILABLE_CIT_REF_FIELDS = {
    "contexts",
    "intents",
    "contextsWithIntent",
    "isInfluential",
    "paperId",
    "corpusId",
    "url",
    "title",
    "venue",
    "publicationVenue",
    "year",
    "authors",
    "externalIds",
    "abstract",
    "referenceCount",
    "citationCount",
    "influentialCitationCount",
    "isOpenAccess",
    "openAccessPdf",
    "fieldsOfStudy",
    "s2FieldsOfStudy",
    "publicationTypes",
    "publicationDate",
    "journal",
    "citationStyles"
}

class NotFoundException(Exception):
    pass

class ServerException(Exception):
    pass

class RateLimitException(Exception):
    pass

DEFAULT_FIELDS = ["paperId", "title", "abstract"]

class SemanticScholarClient():
    def __init__(self, api_key: str) -> None:
        self._headers = { 'X-API-KEY': api_key }

    def get_paper_by_id(self, paper_id: str, fields: list[str] = DEFAULT_FIELDS):
        """
        Retrieves a paper object given its paper ID

        :param paper_id: paper ID of desired paper object
        :param fields: list of desired fields
        """
        self._validate_fields(fields)
        response = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}",
                                headers=self._headers,
                                params={ 'fields': ','.join(fields) })

        if not response.ok:
            if response.status_code == 429:
                raise RateLimitException("Rate limit reached, too many requests")
            else:
                raise ServerException(f'{response.status_code}: {response.text} for paper with ID "{paper_id}"')

        data = response.json()
        if "paperId" not in data:
            raise NotFoundException(f"Could not find: {paper_id}")

        return data
    
    def get_paper_by_title(self, title: str, fields: list[str] = DEFAULT_FIELDS):
        """
        Retrieves the closest match paper object to given title (using `/search/match` endpoint)

        :param title: paper ID of desired paper object
        :param fields: list of desired fields
        """
        self._validate_fields(fields)
        response = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/search/match",
                                headers=self._headers,
                                params={ 'query': title, 'fields': ','.join(fields)})

        if not response.ok:
            if response.status_code == 429:
                raise RateLimitException("Rate limit reached, too many requests")
            else:
                raise ServerException(f'{response.status_code}: {response.text} for paper with title "{title}"')

        data = response.json()
        if "data" not in data:
            raise NotFoundException(f"Could not find: {title}")

        return data["data"][0]

    def get_citations_by_paper_id(self, paper_id: str, fields: list[str] = DEFAULT_FIELDS):
        """
        Retrieves paper objects that cite the paper with the given paper ID

        :param paper_id: paper ID of paper to retrieve citations of
        :param fields: list of desired fields
        """
        self._validate_fields(fields, AVAILABLE_CIT_REF_FIELDS)
        response = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations",
                                headers=self._headers,
                                params={ 'fields': ','.join(fields) })

        if not response.ok:
            if response.status_code == 429:
                raise RateLimitException("Rate limit reached, too many requests")
            else:
                raise ServerException(f'{response.status_code}: {response.text} for citations of paper ID "{paper_id}"')

        data = response.json()
        if "data" not in data:
            raise NotFoundException(f"Could not find: {paper_id}")

        return data["data"]

    def get_references_by_paper_id(self, paper_id: str, fields: list[str] = DEFAULT_FIELDS):
        """
        Retrieves paper objects that is referenced by the paper with the given paper ID

        :param paper_id: paper ID of paper to retrieve references from
        :param fields: list of desired fields
        """
        self._validate_fields(fields, AVAILABLE_CIT_REF_FIELDS)
        response = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references",
                                headers=self._headers,
                                params={ 'fields': ','.join(fields) })

        if not response.ok:
            if response.status_code == 429:
                raise RateLimitException("Rate limit reached, too many requests")
            else:
                raise ServerException(f'{response.status_code}: {response.text} for references of paper ID "{paper_id}"')

        data = response.json()
        if "data" not in data:
            raise NotFoundException(f"Could not find: {paper_id}")

        return data["data"]

    def _validate_fields(self, fields: list[str], valid_fields: set[str] = AVAILABLE_FIELDS) -> None:
        """
        Checks whether given list of strings are valid field names, if not then raises an exception

        :param fields: list of fields to validate
        :param valid_fields: list of valid fields
        """
        invalid_fields = []
        for field in fields:
            if field not in valid_fields:
                invalid_fields.append(field)

        if invalid_fields:
            raise Exception(f'The following fields are invalid: {",".join(invalid_fields)}')
