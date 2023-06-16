from pathlib import Path
import textwrap

class RecipeBox:
    # define constructor and implement prgram flow
    def __init__(self):
        # path
        __path = "C:/Users/Ayomide/Desktop/Development/Python/Python_refresh/recipe_box/Recipes"
        # convert path type
        self.__recipe_dir = Path(__path)
        # count how many recipe files available in recipe dir and sub-dir
        __recipe_count = 0
        for recipe in list(self.__recipe_dir.glob('**/*.txt')):
            __recipe_count += 1
        
        #welcome user
        # Tell user the Path to dir where recipe box is located
        # display how many recipes are available
        welcome_str = (f"""
              *****************************************
              Hi Chef👩🏽‍🍳 - Weclome to your Recipe Box🥩
              
              Your Recipes are located at:
               
              {self.__recipe_dir}
              
              There are {__recipe_count} total recipes
              
              Input a number to select menu option
              ____________________________________ 
              """)
        # remove whitespace space and print
        print(textwrap.dedent(welcome_str))
        
        # create a list of menu options
        menu_options =  ('read recipe', 'create recipe', 'create category', 'delete recipe', 'exit')
        # print out the list for user
        for index, option in enumerate(menu_options):
            print(f'{option} - {index + 1}')
        
        self.select_menu_option()
        
    # return user choice to select a menu option  
    def select_menu_option(self, menu_options: list) -> int:
        select_menu_option = None
        while select_menu_option not in range(len(menu_options) + 1):
            select_menu_option = int(input('Choose one of the Options: '))
        return select_menu_option             
        
    
    def choose_category(self, category):
        # goes into the folders and select a cat
        # returns a folder with list of recipe
        pass
    
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

