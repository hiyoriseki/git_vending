import os
import sqlite3

conn = sqlite3.connect('Vending.db')
cur = conn.cursor()
flg = None

while flg == None:
    print("1.編集", "2.購入", "3.終了")
    menu_select = int(input('実行したいメニューを番号でお選び下さい:'))

    while True:
        if menu_select == 1:
            print('1.商品追加','2.商品在庫数','3.商品価格','4.商品削除','5.終了')
            menu_select2 = int(input('実行したいメニューを番号でお選び下さい:'))
            # 商品追加
            if menu_select2 == 1:
                try:
                    insert_drink = input('追加する商品名を入力してください:')
                    insert_price = int(input('追加する商品の値段を入力してください:'))
                    insert_amount = int(input('追加する商品の在庫数を入力してください:'))
                    cur.execute('INSERT INTO Edit values(?,?,?)',[insert_drink, insert_price,insert_amount])
                except:
                    print('数値を入力してください')

            #商品在庫数編集
            elif menu_select2 == 2:
                cur.execute('SELECT * FROM edit')
                drinks = cur.fetchall()
                drinklist = []
                for i in drinks:
                    drinklist.append("{}:{}個".format(i[0],i[2]))
                print(*drinklist)
                select = input('在庫数変更をする商品名を入力してください:')
                exist_flg = None
                for i in drinks:
                    if i[0] == select:
                        exist_flg = "exist"
                        break
                    else:
                        continue
                ##存在しない商品/数字が入力された時
                if exist_flg != None:
                    cur.execute('SELECT * FROM edit')
                else:
                    print('入力された商品は存在しません')

                #在庫入力
                if exist_flg != None:
                    insert_amount2 = input('在庫数を入力してください:')
                    if insert_amount2.isdigit():
                        cur.execute('update edit set amount = ? where drinks = ?',(insert_amount2,select))
                    else: #数字以外が入力された時
                        print('数値を入力してください')

                else:
                    print()


            #商品価格
            elif menu_select2 == 3:
                cur.execute('SELECT * FROM edit')
                drinks = cur.fetchall()
                drinklist = []
                for i in drinks:
                    drinklist.append("{}:{}円".format(i[0], i[1]))
                print(*drinklist)
                #編集商品の選択
                select = input('編集するドリンク名を入力してください:')
                exist_flg = None
                for i in drinks:
                    if i[0] == select:
                        exist_flg = "exist"
                        break
                    else:
                        continue
                #存在しない商品/数字が入力された時
                if exist_flg != None:
                    cur.execute('SELECT * FROM edit')
                else:
                    print('入力された商品は存在しません')

                #価格入力
                if exist_flg != None:
                    insert_price2 = input('商品の値段を入力してください:')
                    if insert_price2.isdigit():
                        cur.execute('update from edit set price = ? where drinks = ?',(insert_price2,select))
                    else: #数字以外が入力された時
                        print('数値を入力してください')

            elif menu_select2 == 4:
                cur.execute('SELECT * FROM edit')
                drinks = cur.fetchall()
                drinklist = []
                for i in drinks:
                    drinklist.append("{}".format(i[0]))
                print(*drinklist)
                delete = input('削除する商品名を入力してください:')
                exist_flg = None
                for i in drinks:
                    if i[0] == delete:
                        exist_flg = "exist"
                        break
                    else:
                        continue

                if exist_flg != None:
                    cur.execute('delete from edit where drinks = ?',(delete,))
                else:
                    print('入力された商品は存在しません')

            else:
                print('メニュー画面に戻りますか:')
                while True:
                    loop = input('Yes or No:')
                    if loop == 'Yes':
                        os.system('clear')
                        break
                    elif loop == 'No':
                        # sys.exit()
                        flg = 'End'
                        break
                    else:
                        print('Yes or Noで再度入力してください')
                        continue

        else:
            break
        break
