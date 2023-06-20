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
              
              """)
        # remove whitespace space and print
        print(textwrap.dedent(_welcome_str))
        
        # display main menu for the app
        user_menu_choice = self.display_main_menu()
        
        _exit_program = False
        while not _exit_program:  
            # let user read recipe
            if user_menu_choice == 1:
                self.read_recipe(_recipe_dir)
                # go back to main menu
                user_menu_choice = self.display_main_menu()

            # let user create new recipe
            if user_menu_choice == 2:
                self.create_recipe(_recipe_dir)
                # go back to main menu
                user_menu_choice = self.display_main_menu()
        
            # let user create new recipe category
            if user_menu_choice == 3:
                self.create_category(_recipe_dir)
                # go back to main menu
                user_menu_choice = self.display_main_menu()
        
            # let user delete recipes
            if user_menu_choice == 4:
                self.delete_recipe(_recipe_dir)
                # go back to main menu
                user_menu_choice = self.display_main_menu()
        
            # let user delete category
            if user_menu_choice == 5:
                self.delete_category(_recipe_dir)
                # go back to main menu
                user_menu_choice = self.display_main_menu()
            
            # break out of the program
            if user_menu_choice == 6:
                _exit_program = True
            
        
    # print user options  
    def _print_options(self, options:list) -> None:
        # print out list for user
        for index, choice in enumerate(options):
            print(f'{choice} - {index + 1}')
    
    # return user choice 
    def _select_option(self, options:list) -> int:
        option = None
        while option not in range(len(options) + 1):
            option = int(input('Choose one of the Options: '))
        return option             
        
    # func to return a path
    def _navigate_directory(self, base_directory:Path) -> Path:
        # store all folder/file name in base_dir as a list
        all_folders =  [item.name for item in base_directory.iterdir()]
        # print all available folder name for user to choose from
        self._print_options(all_folders)
        # accept input on what folder user needs to access
        user_choice = self._select_option(all_folders)
        # if folder name is same as user choice
        # return new path
        for index, category in enumerate(all_folders):
            if index + 1 == user_choice:
                return Path(f'{base_directory}\{all_folders[index]}')
            
    def display_main_menu(self):
        print('Input a number to select menu option')
        print('____________________________________ ')
        # list of menu options
        _menu_options =  ['read recipe', 'create recipe', 'create category', 'delete recipe', 'delete category', 'exit']
        # print user options
        self._print_options(_menu_options)
        # accept user input to pick an option
        user_menu_choice = self._select_option(_menu_options)
        return user_menu_choice
    
    def read_recipe(self, recipe_path:Path) -> None:
        # if user wants to read a recipe
        print('\nChoose Category of recipe to read')
        # navigate to user recipe category
        user_category_choice = self._navigate_directory(recipe_path)
        print('\nChoose recipe to read')
        # navigate to user recipe
        user_recipe_choice = self._navigate_directory(user_category_choice)
        print('*****************************')
        # Open the file in read mode
        with open(user_recipe_choice, 'r') as file:
            # Read the contents of the file
            print(f'\n{file.read()}\n')
        print('*****************************')
    
    def create_recipe(self, recipe_path:Path) -> None:
        print('\nChoose Category to create recipe in')
        recipe_category = self._navigate_directory(recipe_path)
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
            print('*****************************')
            print('SUCCESS🎉 - Recipe Created')
            print('*****************************')
    
    def create_category(self, category_path:Path) -> None:
        category_name = input('\nEnter Category Name: ')
        new_category_path = Path(f'{category_path}/{category_name}')
        while new_category_path.exists():
            print('\Category already exists')
            category_name = input('Type new Category name: ')
        new_category_path.mkdir(parents=True, exist_ok=True)
        print('*****************************')
        print('SUCCESS🎉 - Folder Created')
        print('*****************************')
    
    def delete_recipe(self, recipe_path:Path) -> None:
        # locate the recipe to delete
        category_to_delete_from = self._navigate_directory(recipe_path)
        recipe_to_delete = self._navigate_directory(category_to_delete_from)
        # delete the file
        recipe_to_delete.unlink()
        print('*****************************')
        print('SUCCESS🎉 - Recipe Deleted')
        print('*****************************')
    
    def delete_category(self, category_path:Path) -> Path:
        # choose directory to delete
        print('\nChoose Category to delete')
        category_to_delete = self._navigate_directory(category_path)
        # if category contains recipe, then delete them first
        if not len(list(category_to_delete.iterdir())) == 0:
            for item in category_to_delete.glob('*'):
                item.unlink()
        # delete the directory itself
        category_to_delete.rmdir()
        print('*****************************')
        print('SUCCESS🎉 - Category Deleted')
        print('*****************************')
   
   
   
# initiate class
recipe_box = RecipeBox()

