Feature: Creating web content
	Producers can add, edit and remove web content

	Background:
		Given Producer is logged in

		# 1
		Scenario Outline: Displaying adding form
			Given Destination folder is displayed
			When Producer chooses Add new
			And Producer chooses <item>
			Then <item> form is displayed

			Examples:
				| item |
				| Use Case |
				| Test Case |
				| Method |
				| Tool |
				| Requirement |
				| Evaluation Scenario |

		# 2
		Scenario Outline: Adding items
			Given <item> form is displayed
			And Required fields are filled
			When Producer saves <item>
			Then <item> is in destination folder

			Examples:
				| item |
				| Use Case |
				| Test Case |
				| Method |
				| Tool |
				| Requirement |
				| Evaluation Scenario |

		# 3
		Scenario Outline: Displaying editting form
			Given <item> page is displayed
			When Producer chooses Edit
			Then <item> form is displayed

			Examples:
				| item |
				| Use Case |
				| Test Case |
				| Method |
				| Tool |
				| Requirement |
				| Evaluation Scenario |

		# 4
		Scenario Outline: Editing items
			Given <item> form is displayed
			And Required fields are filled
			When Producer saves <item>
			Then <item> is edited

			Examples:
				| item |
				| Use Case |
				| Test Case |
				| Method |
				| Tool |
				| Requirement |
				| Evaluation Scenario |

		# 5
		Scenario Outline: Displaying Contents page of item folder
			Given <item> page is displayed
			When Producer choose Contents
			Then Contents of <item> folder is displayed

			Examples:
				| item |
				| Use Case |
				| Test Case |
				| Method |
				| Tool |
				| Requirement |
				| Evaluation Scenario |

		# 6
		Scenario Outline: Removing items
			Given Contents of <item> folder is displayed
			And <item> is checked
			When Producer clicks on Delete button
			Then <item> is removed

			Examples:
				| item |
				| Use Case |
				| Test Case |
				| Method |
				| Tool |
				| Requirement |
				| Evaluation Scenario |
