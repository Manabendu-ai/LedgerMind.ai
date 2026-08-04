from fastapi import UploadFile
import os


class FileService:

    async def save(self, file: UploadFile, persist_dir: str = "docs/"):
        try:
            os.makedirs(persist_dir, exist_ok=True)
            filename = file.filename
            file_path = os.path.join(persist_dir, filename)
            content = await file.read()
            with open(file_path, "wb") as f:
                f.write(content)
            return file_path

        except Exception as e:
            print(f"Exception at FileService : {e}")