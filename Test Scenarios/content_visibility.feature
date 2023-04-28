Feature: Content publishing
	Producers can change the visibility of web content 

	Background:
		Given Producer is logged in

		# 11
		Scenario: Producer can publish content for every user
			Given Page for publishing is displayed
			When Producer chooses State
			And Producer chooses Public
			Then Page is public
		# 12
		Scenario Outline: Producer can hide content
			Given Page for hiding is displayed
			When Producer chooses State
			And Producer chooses <option>
			Then Page is private

			Examples:
				| option |
				| Send Back |
				| Retract |