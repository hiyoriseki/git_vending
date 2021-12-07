from vending_dbclass import Vendings, Choice_0, Choice_1, Choice_2, Choice_3, Choice_4

vendings = Vendings()
menu_select = vendings.select_1()

choice_0 = Choice_0()
menu_select2 = choice_0.menu_choice(menu_select)


choice_1 = Choice_1()
menu_select2 = choice_1.edit_insert(menu_select2)
