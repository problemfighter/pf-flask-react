import os
import subprocess

application_dir = "application"
xyz12_lib_dir = "xyz12"
pf_flask_source = "pf-flask"


def get_git():
    git = "git"
    exported_git_path = os.environ.get('git_path')
    if exported_git_path:
        git = "\"" + exported_git_path + "\""
    return git


def git_command(command):
    return get_git() + " " + command


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_directories(directory_list: list):
    for directory in directory_list:
        create_directory(directory)


def execute_command(home, command):
    subprocess.run(command, shell=True, cwd=home)


def pull_project(home):
    git_directory = home + "/.git"
    if os.path.exists(git_directory):
        execute_command(home, git_command("pull"))


def clone_project(root, project, url):
    if url != "":
        command = git_command("clone ") + url + " " + project
        execute_command(root, command)


def setup_project(home):
    module_directory = home + "/setup.py"
    if os.path.exists(module_directory):
        execute_command(home, "python setup.py develop")


def clone_and_setup(root, project, url, path):
    if not os.path.exists(path):
        clone_project(root, project, url)
        setup_project(path)


def pull_setup_project(home):
    pull_project(home)
    setup_project(home)


def clone_pull_setup(projects: dict):
    root = projects['dir']
    create_directory(root)
    repositories: dict = projects['repositories']
    repository_names = repositories.keys()
    for name in repository_names:
        print("\n\n\n\n-------------------------------------------------------------------------------------")
        print("Working with repository: " + name + ", source: " + root)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        path = os.path.join(root, name)
        repository = repositories.get(name)
        clone_and_setup(root, name, repository, path)
        pull_setup_project(path)
        print("-------------------------------------------------------------------------------------")


source_projects = {
    "dir": xyz12_lib_dir,
    "repositories": {
        pf_flask_source: "https://github.com/problemfighter/pf-flask.git",
    }
}


def configure_pf_flask_source():
    path = os.path.join(xyz12_lib_dir, pf_flask_source)
    if os.path.exists(path):
        command = "bash tools/prepare-dev.sh"
        execute_command(path, command)


def pull_and_setup_application_modules():
    print("\n\n\n\n-------------------------------------------------------------------------------------")
    print("Taking Application Module Pull")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if os.path.exists(application_dir):
        pull_project(application_dir)
        for directory in os.listdir(application_dir):
            path = os.path.join(application_dir, directory)
            if os.path.isdir(path):
                print("\n\n\n\n################################################################################")
                print("Taking pull and setup of " + directory)
                print("################################################################################")
                pull_setup_project(path)


def start():
    clone_pull_setup(source_projects)
    pull_project("./")
    pull_and_setup_application_modules()
    configure_pf_flask_source()


if __name__ == '__main__':
    start()
