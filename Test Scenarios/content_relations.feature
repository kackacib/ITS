Feature: Entity relations 
	Producers can add, edit and remove relations between web content entities

	Background:
		Given Producer is logged in

		# 7
		Scenario: Link Use Case with Evaluation Scenario
			Given Use Case form is displayed
			And Use Case Evaluation Scenarios panel is chosen
			And Link to Evaluation Scenario is filled
			When Producer saves Use Case
			Then Relation between Use Case and Evaluation Scenario is created

		# 8
		Scenario: Link Method with Tool and Test Case
			Given Method form is displayed
			And Relations panel is chosen
			And Link to Tool is filled
			And Link to Test Case is filled
			When Producer saves Method
			Then Relation between Method and Tool is created
			And Relation between Method and Test Case is created

		# 9
		Scenario: Link Evaluation Scenario with 2 Requirements
			Given Evaluation Scenario form is displayed
			And Evaluation Scenario Requirements panel is chosen
			And Evaluation Scenario Requirements List has 2 links
			When Producer saves Evaluation Scenario
			Then Relation between Evaluation Scenario and Requirement is created

		# 10
		Scenario: Remove relation between Use case and 1 Evaluation Scenario
			Given Use case form is displayed
			And Use Case Evaluation Scenarios panel is chosen
			And Evaluation Scenarios List is filled
			When Producer removes 1 link from Evaluation Scenarios List
			And Producer saves Use Case
			Then Relation between Use Case and 1 Evaluation Scenario is removed