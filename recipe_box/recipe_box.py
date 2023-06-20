from pathlib import Path
import textwrap

class RecipeBox:
    # define constructor and implement prgram flow
    def __init__(self):
        # path
        _recipe_dir = Path("C:/Users/Ayomide/Desktop/Development/Python/Python_refresh/recipe_box/Recipes")
        # count how many recipe files available in recipe dir and sub-dir
        _recipe_count = 0
        for recipe in list(_recipe_dir.glob('**/*.txt')):
            _recipe_count += 1
        
        #welcome user
        # Tell user the Path to dir where recipe box is located
        # display how many recipes are available
        _welcome_str = (f"""
              *****************************************
              Hi Chef👩🏽‍🍳 - Weclome to your Recipe Box🥩
              
              Your Recipes are located at:
               
              {_recipe_dir}
              
              There are {_recipe_count} total recipes
              
              Input a number to select menu option
              ____________________________________ 
              """)
        # remove whitespace space and print
        print(textwrap.dedent(_welcome_str))
        
        # list of menu options
        _menu_options =  ['read recipe', 'create recipe', 'create category', 'delete recipe', 'exit']
        # list of categories in directory
        # categories = [category.name for category in __recipe_dir.iterdir() if category.is_dir()]
        # print user options
        self._print_options(_menu_options)
        # accept user input to pick an option
        user_menu_choice = self.select_option(_menu_options)
        
        # if user wants to read a recipe
        if user_menu_choice == 1:
            print('\nChoose Category of recipe to read')
            # navigate to user recipe category
            user_category_choice = self.navigate_directory(_recipe_dir)
            print('\nChoose recipe to read')
            # navigate to user recipe
            user_recipe_choice = self.navigate_directory(user_category_choice)
            # Open the file in read mode
            with open(user_recipe_choice, 'r') as file:
                # Read the contents of the file
                print(f'\n{file.read()}\n')
        # let user create new recipe
        if user_menu_choice == 2:
            print('\nChoose Category to create recipe in')
            recipe_category = self.navigate_directory(_recipe_dir)
            # check if chosen option is a valid folder
            if recipe_category.is_dir():
                # collect recipe name from user
                recipe_name = input('\nType new recipe name: ')
                # concatenate chosen category and recipe name into single path
                new_recipe_path = Path(f'{recipe_category}/{recipe_name}.txt')
                # prevent duplicate recipe name
                while new_recipe_path.exists():
                    print('\nRecipe name already exists')
                    recipe_name = input('Type new recipe name: ')
                # store recipe content
                recipe_content = input('\nType recipe content: ')
                # create new recipe file and write content to it
                with open(new_recipe_path, 'w') as new_recipe:
                    new_recipe.write(recipe_content)
                print('SUCCESS🎉 - Recipe Created')
                
                    
            
            
        
    # print user options  
    def _print_options(self, options:list) -> None:
        # print out list for user
        for index, choice in enumerate(options):
            print(f'{choice} - {index + 1}')
    
    # return user choice 
    def select_option(self, options:list) -> int:
        option = None
        while option not in range(len(options) + 1):
            option = int(input('Choose one of the Options: '))
        return option             
        
    # func to return a path
    def navigate_directory(self, base_directory:Path) -> Path:
        # store all folder/file name in base_dir as a list
        all_folders =  [item.name for item in base_directory.iterdir()]
        # print all available folder name for user to choose from
        self._print_options(all_folders)
        # accept input on what folder user needs to access
        user_choice = self.select_option(all_folders)
        # if folder name is same as user choice
        # return new path
        for index, category in enumerate(all_folders):
            if index + 1 == user_choice:
                return Path(f'{base_directory}\{all_folders[index]}')
    
    def choose_recipe(self, category, recipe_name):
        # return a recipe path
        pass
    
    def read_recipe(self, category, recipe_name):
        # call choose_recipe and read the content
        pass
    
    def create_recipe(self, category, recipe_name, content):
        # run choose_category() for user 
        # to pic a category
        # collect name and content of new recipe
        # append to cat folder
        pass
    
    def create_category(self, category_name):
        # recieves a category name
        # and creates it
        pass
    
    def delete_recipe(self, category, recipe_name):
        # call choose_recipe and delete the result
        pass
    
    def exit_program(self):
        # break out of the whole loop
        pass
   
# initiate class
recipe_box = RecipeBox()
# list all folders in a dir
# p = Path('./recipe_box/Recipes')
# print ([x for x in p.iterdir() if x.is_dir()])

# listing python files in the sub-dir
# print(list(p.glob('**/*.txt')))

# path boolean
# print(p.exists())

# read contents
# with p.open() as f:
#     print(f.readline())

# print(str(p))
# print(p.suffix)
# print(p.suffixes)
# print(p.name)
# print(p.parent)
# print(p.match('*.txt'))
# PureWindowsPath('c:').joinpath('/Program Files')

# print(Path.cwd)

