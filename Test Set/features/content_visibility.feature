Feature: Content publishing
	Producers can change the visibility of web content 

	Background:
		Given Producer is logged in

		# 12
		Scenario: Producer can hide content
			Given Page for hiding is displayed
			When Producer chooses State
			And Producer chooses Send Back
			Then Page is private
			
		# 11
		Scenario: Producer can publish content for every user
			Given Page for publishing is displayed
			When Producer chooses State
			And Producer chooses Publish
			Then Page is public

