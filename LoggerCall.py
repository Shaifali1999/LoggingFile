from LoggerLib import LoggerLib

__author__ = "Shaifali Rao"

# Calling **LoggerLib** function
file_name = 'SHAIFALI'
lib_obj = LoggerLib()
log_obj = lib_obj.logger_func(file_name)
log_obj.info("I am from logger call class".format())
log_obj.critical("CRIC".format())
log_obj.error("ERR".format())
log_obj.warning("WARN".format())
log_obj.debug("debug".format())
log_obj.info("qwerty".format())
log_obj.info("asdfghjkl".format())
log_obj.info("End".format())
log_obj.info("Hi This is Shaifali Rao")
# closing file
log_obj.handlers.clear()
lib_obj1 = LoggerLib()
log_obj1 = lib_obj1.logger_func('shaifali')
log_obj1.info('hello')
# log_obj1.handlers.clear()


import argparse

# Argparse
arg_obj = argparse.ArgumentParser("ipconfig test")
arg_obj.add_argument('--run-hardcoded-output', type=str, choices=['true', 'false'],
                     dest='run_hardcoded_output', required=False, default='true',
                     help='Default as true, Run only test hardcoded output if argument as "true", '
                          'Run the actual cmd on system if argument as "false"')
get_parse = arg_obj.parse_args()
hardcoded_output = get_parse.run_hardcoded_output
print("Hardcoded_output(Args Value): ", hardcoded_output)