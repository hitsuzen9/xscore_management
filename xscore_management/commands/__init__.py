def get_commands():
	# prevent circular imports
	from .command_test import commands as command_test_commands

	all_commands = (
		command_test_commands
	)

	return all_commands

commands = get_commands()
