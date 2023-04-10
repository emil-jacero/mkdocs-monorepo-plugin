import os
import tempfile
from git import Repo


class GitClone:
    def __init__(self, git_url, git_ref):
        self.git_url = git_url
        self.git_ref = git_ref

    def clone(self):
        temp_dir = tempfile.mkdtemp()
        repo = Repo.clone_from(self.git_url, temp_dir, branch=self.git_ref)
        return temp_dir
