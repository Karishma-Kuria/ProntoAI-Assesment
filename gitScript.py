import git
from git import InvalidGitRepositoryError
import sys
import os
from datetime import datetime
from datetime import date
from datetime import timedelta

'''
    Class for the functions to run git commands in python script.
'''
class gitIntegration:
    def __init__(self):
        # get the local git repo
        self.repo = self.validatePath()

    '''
        This function validates the local git repo path provided as the argument to the script
        and returns the object of the local git repo.
    '''
    def validatePath(self):
        # get the git local directory path from the arguments
        if len(sys.argv) >= 2 and sys.argv[1] != "":
            # check if the local directory path provided exists
            isExist = os.path.exists(sys.argv[1])
            if isExist: 
                # load the git repository
                try:
                    repo = git.Repo(sys.argv[1])
                    return repo
                except InvalidGitRepositoryError:
                    # raise exception when there is no git repository in the given path
                    raise InvalidGitRepositoryError("The local directory contains no git repository.")
            # raise exception if the git directory path does not exists
            else:
                raise Exception("Local git directory path does not exists. Please provide valid path.")
        # raise exception if the git directory path is not provided in the argument
        else:
            raise Exception("Please provide local git directory path as the argument.")


    '''
        This function get the active branch of the current repo.
        We can also use "repo.active_branch" to get the active branch.
        It returns the name of the active branch.
    '''
    def getActiveBranch(self):
        branch = self.repo.head.reference
        return branch

    ''' Check if any files in the current branch is changed and returns a boolean value. 
        This works as git status and provides the list of changed files.'''
    def filesModified(self):
        changedFiles = [ item.a_path for item in self.repo.index.diff(None) ]
        if len(changedFiles)==0:
            return False
        else:
            return True
    
    '''
        Get all the commits for the active branch. This function will give us the list of all the commits in a chronological order 
        of the current branch with the latest commit first.
        This function returns a boolean value value indicating if the last commit was authored in the last week.
    '''
    def getRecentCommit(self, branch):
        # gets the list of the details of all the commit for given branch
        commits = list(self.repo.iter_commits(branch))
        # get today's date
        today = date.today() 
        # list to store the dates from last 7 days
        dateset = []
        # get all the dates for last 7 days
        for i in range(0,7):
            dateset.append(today - timedelta(days=i))
        commit_date = datetime.strptime(commits[0].committed_datetime.strftime('%Y-%m-%d'), '%Y-%m-%d').date()
        # check if the last commit date is from last week
        if commit_date in dateset:
            return True
        else:
            return False
    """
        Get the name of the author for the latest commit and check if it's Lufus.
        This function returns a boolean value.
    """
    def getAuthor(self, branch):
        # gets the list of the details of all the commit for given branch
        commits = list(self.repo.iter_commits(branch))
        # get the author name
        author_name = commits[0].author
        # check if its "Rufus"
        if str(author_name) != "Rufus":
            return False
        else:
            return True

if __name__ == "__main__":
    try:
        # create object of the class
        gitIntegrationObj = gitIntegration()
        # get active branch
        active_branch = gitIntegrationObj.getActiveBranch()
        # check if repository files have been modified
        local_changes = gitIntegrationObj.filesModified()
        # check whether the current head commit was authored in last week
        recent_commit = gitIntegrationObj.getRecentCommit(active_branch)
        # check whether the current head commit was authored by Rufus
        blame_lufus = gitIntegrationObj.getAuthor(active_branch)

        # print the output
        print("active branch:", active_branch)
        print("local changes:", str(local_changes))
        print("recent commit:", str(recent_commit))
        print("blame Rufus:", str(blame_lufus))
    except Exception as ex:
        print(ex)
