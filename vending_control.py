from vending_dbclass import Vendings, Choice_0, Choice_1, Choice_2, Choice_3, Choice_4

vendings = Vendings()
menu_select = vendings.select_1()

choice_0 = Choice_0()
menu_select2 = choice_0.menu_choice(menu_select)


choice_1 = Choice_1()
menu_select2 = choice_1.edit_insert(menu_select2)

choice_2 = Choice_2()
menu_select2 = choice_2.edit_stock(menu_select2)

choice_3 = Choice_3()
menu_select2 = choice_3.edit_price(menu_select2)

choice_4 = Choice_4()
menu_select2 = choice_4.edit_delete(menu_select2)
