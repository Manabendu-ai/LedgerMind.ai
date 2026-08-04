from langchain_community.document_loaders import UnstructuredMarkdownLoader, TextLoader
from pathlib import Path
from typing import List, Any


class DocumentLoader:
    def load_all_documents(self, dir : str = "md_files/")->List[Any]:
        path = Path(dir).resolve()
        docs = []

        md_files = list(path.glob("**/*.md"))
        for md_file in md_files:
            try:
                loader = UnstructuredMarkdownLoader(str(md_file))
                loaded = loader.load()
                docs.extend(loaded)
            except Exception as e:
                print(f"[EXCEPTION] Data Loader {e}")

        return docs