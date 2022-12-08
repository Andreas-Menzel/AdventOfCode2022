
class Filesystem():
    root_directory = None

    def __init__(self):
        self.root_directory = Directory('~#ROOT_DIRECTORY#~')

    def add_directory(self, _path, _directory):
        dir_path_end = None
        if _path == '/':
            dir_path_end = self.root_directory
        else:
            dir_path_end = root_directory.traverse_path(_path)
        
        dir_path_end.add_directory(_directory)
    
    def add_file(self, _path, _file):
        if _path == '/':
            dir_path_end = self.root_directory
        else:
            dir_path_end = root_directory.traverse_path(_path)
        
        dir_path_end.add_file(_file)
    
    def calculate_size(self):
        self.root_directory.calculate_size()


class Directory():
    def __init__(self, _dirname):
        self.dirname = _dirname

        self.dirsize = 0
        self.totalsize = 0 # According to challenge one
        self.parent_directory = None
        self.files = {}
        self.subdirectories = {}

        #print(f'Created directory "{self.dirname}"')
    
    def set_parent_directory(self, _parent_directory):
        self.parent_directory = _parent_directory
    
    def calculate_size(self):
        size = 0

        for (filename, file) in self.files.items():
            size = size + file.filesize
        
        for (dirname, directory) in self.subdirectories.items():
            directory.calculate_size()
            size = size + directory.dirsize
        
        self.dirsize = size

    def add_file(self, _file):
        # Yes, I know. Saving the file name at two different locations is
        # not optimal. But since directories cannot be renamed in this example,
        # it's fine with me.
        self.files[_file.filename] = _file
        #print(f'Added file "{_file.filename}" in "{self.dirname}".')
    
    def add_directory(self, _directory):
        # Yes, I know. Saving the directory name at two different locations is
        # not optimal. But since directories cannot be renamed in this example,
        # it's fine with me.
        _directory.set_parent_directory(self)
        self.subdirectories[_directory.dirname] = _directory
        #print(f'Added directory "{_directory.dirname}" in "{self.dirname}".')
    
    def traverse_path(self, _path):
        if _path == '':
            return self
        
        # remove first and last slash
        path_split = _path.split('/', 1)

        next_step = path_split[0]
        
        remaining_steps = ''
        if len(path_split) > 1:
            remaining_steps = path_split[1]

        try:
            next_directory = None

            if next_step == '..':
                next_directory = self.parent_directory
            else:
                next_directory = self.subdirectories[next_step]
            
            return next_directory.traverse_path(remaining_steps)
        except:
            print(f'ERROR: Directory "{self.dirname}" has no subdirectory "{next_step}".')


class File():
    def __init__(self, _filename, _filesize):
        self.filename = _filename
        self.filesize = _filesize


def calculate_total_dir_size(_directory):
    combined_size = 0

    if _directory.dirsize <= 100000:
        combined_size = combined_size + _directory.dirsize

    for (dirname, subdir) in _directory.subdirectories.items():
        combined_size = combined_size + calculate_total_dir_size(subdir)
    
    _directory.totalsize = combined_size

    return combined_size





def main():
    filesystem = Filesystem()
    current_directory = filesystem.root_directory

    # Read terminal history
    terminal_history = []
    with open('input.txt') as terminal_history_file:
        terminal_history = terminal_history_file.readlines()
    terminal_history = [ line.rstrip() for line in terminal_history ]
    
    for cmd in terminal_history:
        #print(f'Begin in dir "{current_directory.dirname}"')
        if cmd[0] == '$':
            if cmd[2:4] == 'cd':
                path = cmd[5:]
                
                if path == '/':
                    current_directory = filesystem.root_directory
                else:
                    current_directory = current_directory.traverse_path(path)
            elif cmd[2:4] == 'ls':
                # Assuming the terminal ALWAYS outputs as intended (1/2)
                pass
        else:
            # Assuming the terminal ALWAYS outputs as intended (2/2)
            ls_output = cmd.split(' ')
            if ls_output[0] == 'dir':
                new_directory = Directory(ls_output[1])
                current_directory.add_directory(new_directory)
            else:
                new_file = File(ls_output[1], int(ls_output[0]))
                current_directory.add_file(new_file)

        #print(f'End in dir "{current_directory.dirname}"')
        #print()
    
    filesystem.calculate_size()

    print(f'Part one: Sum of total sizes is '\
          f'{calculate_total_dir_size(filesystem.root_directory.traverse_path(""))}')



if __name__ == '__main__':
    main()
