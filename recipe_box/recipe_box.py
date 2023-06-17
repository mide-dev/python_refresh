from pathlib import Path
import textwrap

class RecipeBox:
    # define constructor and implement prgram flow
    def __init__(self):
        # path
        __recipe_dir = Path("C:/Users/Ayomide/Desktop/Development/Python/Python_refresh/recipe_box/Recipes")
        # count how many recipe files available in recipe dir and sub-dir
        __recipe_count = 0
        for recipe in list(__recipe_dir.glob('**/*.txt')):
            __recipe_count += 1
        
        #welcome user
        # Tell user the Path to dir where recipe box is located
        # display how many recipes are available
        welcome_str = (f"""
              *****************************************
              Hi Chef👩🏽‍🍳 - Weclome to your Recipe Box🥩
              
              Your Recipes are located at:
               
              {__recipe_dir}
              
              There are {__recipe_count} total recipes
              
              Input a number to select menu option
              ____________________________________ 
              """)
        # remove whitespace space and print
        print(textwrap.dedent(welcome_str))
        
        # list of menu options
        menu_options =  ['read recipe', 'create recipe', 'create category', 'delete recipe', 'exit']
        # list of categories in directory
        categories = [category.name for category in __recipe_dir.iterdir() if category.is_dir()]
        # print user options
        self.print_options(menu_options)
        # accept user input to pick an option
        user_menu_choice = self.select_option(menu_options)
        
        # if user wants to read a recipe
        if user_menu_choice == 1:
            print('\nChoose Category of recipe to read')
            user_category_choice = self.navigate_directory(__recipe_dir)
            print(user_category_choice)
            
                    
            
            
        
    # print user options  
    def print_options(self, options:list) -> None:
        # print out list for user
        for index, choice in enumerate(options):
            print(f'{choice} - {index + 1}')
    
    # return user choice 
    def select_option(self, options:list) -> int:
        option = None
        while option not in range(len(options) + 1):
            option = int(input('Choose one of the Options: '))
        return option             
        
    # func to return a folder path
    def navigate_directory(self, base_directory:Path) -> Path:
        # store all folder name in base_dir as a list
        all_folders =  [item.name for item in base_directory.iterdir() if item.is_dir()]
        # print all available folder name for user to choose from
        self.print_options(all_folders)
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

