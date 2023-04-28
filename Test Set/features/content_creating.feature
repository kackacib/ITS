Feature: Creating web content
	Producers can add, edit and remove web content

	Background:
		Given Producer is logged in

		# 1 - problémy
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

		# 2 edited - problémy
		Scenario: Adding Use Case
			Given Use Case form is displayed
			And Required fields are filled
			When Producer saves Use Case
			Then Use Case is in destination folder

		# 3 edited
		Scenario: Displaying Tool editting form
			Given Tool page is displayed
			When Producer chooses Edit
			Then Tool editting form is displayed

		# 4 removed

		# 5 edited
		Scenario: Displaying Contents page of Method folder
			Given Methods page is displayed
			When Producer choose Contents
			Then Contents of Methods folder is displayed

		# 6 removed

