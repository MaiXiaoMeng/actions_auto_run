import os

SCRIPTS_BASE_DIR = './scripts/'

if __name__ == '__main__':
    for scripts in os.listdir(SCRIPTS_BASE_DIR):
        os.system(f'python ./scripts/{scripts}')
