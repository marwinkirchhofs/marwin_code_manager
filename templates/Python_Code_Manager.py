#!/usr/bin/env python3

# PYTHON PROJECT_CREATE
#
# Create a python project from the template in this directory

import os, re
import Code_Manager

class Python_Code_Manager(Code_Manager.Code_Manager):


    def __init__(self):
        super().__init__("python")
        self.language = "python"


    def __create_main(self, app_name, src_dir):
        
        ##############################
        # READ TEMPLATE FILE
        ##############################

#     with open (TEMPLATES_ABS_PATH_ + "/python/template_main.py", "r") as f_in:
#         template = f_in.readlines()
        template = self._load_template(
                self.TEMPLATES_ABS_PATH + "/template_main.py", 
                app_name, src_dir)

        ##############################
        # ADAPT
        ##############################
        # basically handle the special template placeholders (indicated by 
        # '_TT_*_TT_' instead of '_T_*_T_')

        template_out = []

        for line in template:

            # SOURCE DIRECTORY
            if re.match(r'.*_TT_IMPORT_SRC_DIR_TT_.*', line):
                if src_dir:
                    template_out.extend([
                        "# import " + src_dir + " package\n",
                        "from " + src_dir + " import *\n"
                    ])
                else:
                    pass

            # SOME DUMMY OPTION
            elif re.match(r'some_dummy', line):
                pass

            # NOTHING SPECIAL
            # -> copy the line over
            else:
                template_out.append(line)


        ##############################
        # WRITE PROJECT FILE
        ##############################

        with open (app_name + ".py", "w") as f_out:
            f_out.writelines(template_out)

        # EXECUTION/READ PERMISSIONS
        os.chmod(f"{app_name}.py", (7<<6)+(5<<3)+5)

        return 0


    def __create_init(self, app_name, src_dir):

        # if src_dir is not given, there is no need for an __init__ file, so 
        # just exit
        if not src_dir:
            return 0
        else:
            
            ##############################
            # READ TEMPLATE FILE
            ##############################

            template = self._load_template(
                    self.TEMPLATES_ABS_PATH + "/template_init.py", app_name, 
                    src_dir)

            ##############################
            # CREATE SOURCE DIRECTORY
            ##############################

            # (normally src_dir shouldn't exist, but why not check)
            if not os.path.isdir(src_dir):
                os.mkdir(src_dir)

            ##############################
            # ADAPT
            ##############################
            # basically handle the special template placeholders (indicated by 
            # '_TT_*_TT_' instead of '_T_*_T_')

            template_out = template

            ##############################
            # WRITE PROJECT FILE
            ##############################

            with open (src_dir + "/__init__.py", "w") as f_out:
                f_out.writelines(template_out)

            return 0


    def __create_vimspector(self, app_name, pkg_dir):

        ##############################
        # READ TEMPLATE FILE
        ##############################

        template = self._load_template(
                self.TEMPLATES_ABS_PATH + "/template_vimspector.json", app_name, 
                pkg_dir)

        ##############################
        # ADAPT
        ##############################
        # basically handle the special template placeholders (indicated by 
        # '_TT_*_TT_' instead of '_T_*_T_')

        template_out = list(map(
            lambda s: s.replace("_TT_CWD_TT_", os.getcwd()), template
            ))

        ##############################
        # WRITE PROJECT FILE
        ##############################

        with open (".vimspector.json", "w") as f_out:
            f_out.writelines(template_out)

        return 0

    def _command_package(self, specifier, **args):
        # TODO: implement
        print("herethere")


    def __create_package(self, pkg_name):
        pass


#     def run_code_manager_command(self, command, specifier, **args):
# 
#         # DETERMINE SRC_DIR
#         # TODO: maybe there is a better and more generic spot for this to go to
#         pkg_dir = self._get_str_src_dir(py_pkg) if py_pkg else False
# 
#         # LAUNCH FILE CREATION
#         self.__create_main(app_name, pkg_dir)
#         self.__create_init(app_name, pkg_dir)
#         if vimspector:
#             self.__create_vimspector(app_name, pkg_dir)
#         if git:
#             self._create_git(app_name)
# 
# 
#         return 0
