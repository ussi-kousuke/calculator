from calculator import Calculator
First_number = float(input('数字を入力してください '))
while True:

        question = input('足し算(+) 引き算(-) 掛け算(*) 割り算(/)のうちどれかを選択してください。')
        second_number = float(input('数字を入力してください　'))
        answer = Calculator(First_number, second_number)
        calc_function = {"+": answer.add(),
                         "-": answer.subtract(),
                         "*": answer.multiply(),
                         "/": answer.divide(),
                        }
        final_answer = calc_function[question]
        print(f'計算結果は{final_answer}です。')

        is_calculate = input('まだ計算しますか？　(yes or no) ')
        if is_calculate == 'yes':
                answer.is_calculate()
                First_number = answer.first
                print(First_number)
        else:
                reset_number = input('数字をリセットしますか？ ')
                if reset_number == 'yes':
                        answer.reset()
                        First_number = float(input('数字を入力してください '))
                else:
                        break