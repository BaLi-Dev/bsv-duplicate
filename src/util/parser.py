from dataclasses import dataclass

@dataclass
class Article:
    key: str
    doi: str = None

    def __repr__(self) -> str:
        if self.doi != None:
            return f'{self.key} ({self.doi})'
        else:
            return f'{self.key}'

def parse(data: str) -> list[Article]:
    """
    Parse a raw text file containing bibliographic references in BibTeX format into a list of Article objects.

    :param data: the raw text data to parse
    :return: a list of Article objects
    """
    articles: list[Article] = []

    chunks: list[str] = data.split('@')
    for chunk in chunks[1:]:
        # obtain the key by extracting the string after the article{ prefix of the first line
        lines: list[str] = chunk.split('\n')
        key: str = lines[0].split('{')[1].split(',')[0].strip()

        # obtain the doi by extracting the string after the doi = prefix of the line that contains doi
        doi: str = None
        for line in lines:
            if 'doi' in line:
                doi = line.split('=')[1].strip().replace('{', '').replace('}', '').replace(',', '')
                
        articles.append(Article(key=key, doi=doi))

    return articles