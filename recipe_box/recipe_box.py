from pathlib import Path

class RecipeBox:
    
    # define constructor and implement prgram flow
    def __init__(self):
        # path
        self.__recipe_dir = ("C:\Users\Ayomide\Desktop\Development\Python\Python_refresh/recipe_box/Recipes")
    
        #welcome user
        print("Hi Chef👩🏽‍🍳 - Weclome to your Recipe Box🥩")
        
        # Tell chef the Path to Dir where recipe box is located
        print
    
    def select_option(self):
        # choose option from one to 6
        pass
    
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
    
# list all folders in a dir
# p = Path('./recipe_box/Recipes/Dessert/Brownies.txt')
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