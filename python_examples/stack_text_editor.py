def text_editor():
    text = ''
    stack = []

    while True:
        command = input('Enter "add + <text> to add text, "undo" to undo, or "quit" to exit: ')
        if command.lower().startswith('add '):
            add_text = (' ' + command[4:])
            text += add_text
            stack.append(add_text)
            print(f'Text: {text}')
        elif command.lower() == 'undo':
            if len(stack) == 0:
                print('There is nothing to undo!')
            else:
                remove_text = stack.pop()
                text = text[:-len(remove_text)]
                print(f'Removed text: {remove_text}')
                print(f'Text: {text}')
        elif command == 'quit':
            if len(text) == 0:
                text = '(Empty)'
            print(f'Final Text: {text}')
            break
        else:
            print('Invalid command, please try again')

text_editor()