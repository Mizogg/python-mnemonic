import bip32utils, os, webbrowser, datetime, smtplib
import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path
from mnemonic import Mnemonic
gmail_user = 'YourEmail@gmail.com'
gmail_password = 'YourPassword'
start_time = datetime.datetime.now()

filename ='80000.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)

start_time = datetime.datetime.now()


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}

def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


def create_main_window(settings):
    sg.theme(settings['theme'])

    menu_def = [['&Menu', ['&Settings', 'E&xit']]]
    wordlenght = ['128','192','256']
    divlenght  = ['1','2','3','4','5','10','25','50','100','500','1000']
    layout = [[sg.Menu(menu_def)],
               [sg.Text('🐍 🐍 Mnemonic code for generating deterministic keys, BIP39 Bitcoin Wallet Scanner Off-Line Made by Mizogg in PySimpleGUI 🐍 🐍', size=(40,3), font=('Comic sans ms', 14)),
               sg.Button('', key='mizogg', size=(10,1), font=('Helvetica', 10), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename='mizogg.png', image_size=(400, 80), image_subsample=1, border_width=0)],
               [sg.Text('Total Bitcoin Addresses Looking for : ', size=(35,1), font=('Comic sans ms', 15)),
               sg.Text(line_count, font=('Comic sans ms', 15) , size=(10,1)),
               sg.Button('', key='face', size=(10,1), font=('Helvetica', 30), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename='MizoggFaceBW.png', image_size=(140, 80), image_subsample=1, border_width=0)],
               [sg.Text('HOW MANY WORDS 12=128 18=192 24=256 -> ', size=(38,1), font=('Comic sans ms', 13)),
               sg.Combo(wordlenght, size=(6,1), key='wordstart', background_color='green', text_color='white', font=('Comic sans ms', 13)), sg.Text('', size=(6,1))],
               [sg.Text('How Many Derivation Paths  ✍️ -> ', size=(38,1), font=('Comic sans ms', 13)),
               sg.Combo(divlenght, size=(6,1), key='divs', background_color='green', text_color='white', font=('Comic sans ms', 13)), sg.Text('', size=(6,1)),
              sg.Button('Start/Stop',  font=('Comic sans ms', 14))],
              [sg.Text('')],
              [sg.Output(size=(90, 16), font=('Comic sans ms', 11), key='out')]]

    return sg.Window('MIZOGG WordChoice.py',
                     layout=layout,
                     default_element_size=(8,1))


def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    generator = False
    while True:
        if window is None:
            window = create_main_window(settings)
        event, values = window.Read(timeout=10)
        if event in (None, 'Exit'):
            break
        elif event == 'Start/Stop':
            generator = not generator
            def data_wallet():
                for child in range(0,divs):
                    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
                    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
                        44 + bip32utils.BIP32_HARDEN
                    ).ChildKey(
                        0 + bip32utils.BIP32_HARDEN
                    ).ChildKey(
                        0 + bip32utils.BIP32_HARDEN
                    ).ChildKey(0).ChildKey(child)
                    data.append({
                            'path': f"m/44'/0'/0'/0/{child}",
                            'address': bip32_child_key_obj.Address(),
                            'privatekey': bip32_child_key_obj.WalletImportFormat(),
                        })
            count=0
            total=0
            divs = int(values['divs'])

        if generator:
            data = []
            count += 1
            total += divs
            mnemo = Mnemonic("english")
            mnemonic_words = mnemo.generate(strength=int(values['wordstart'])) # 128 12words / 256 24words / randomwords
            #mnemonic_words = 'assist air special hunt slogan daughter spy reunion winter boost alpha among steak space father situate ahead floor door prison aware demand cross shine' # 17MdcGxXXFWuRPBpd4NDr2vWTCwmAtJrHK
            seed = mnemo.to_seed(mnemonic_words, passphrase="")
            data_wallet()
            for target_wallet in data:
                address = target_wallet['address']
                if address in add:
                    print('\nMatch Found')
                    print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
                    print('\nmnemonic_words  : ', mnemonic_words)
                    print('Derivation Path : ', target_wallet['path'], ' : Bitcoin Address : ', target_wallet['address'])
                    print('Privatekey WIF  : ', target_wallet['privatekey'])
                    with open("winner.txt", "a") as f:
                        f.write(f"""\nMnemonic_words:  {mnemonic_words}
                        Derivation Path:  {target_wallet['path']}
                        Privatekey WIF:  {target_wallet['privatekey']}
                        Public Address Bitcoin:  {target_wallet['address']}
                        =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====""")
                        sent_from = gmail_user
                        to = ['YourEmail@gmail.com']
                        subject = ['OMG Super Important Message']
                        body = f"""\nMnemonic_words:  {mnemonic_words}
                        Derivation Path:  {target_wallet['path']}
                        Privatekey WIF:  {target_wallet['privatekey']}
                        Public Address Bitcoin:  {target_wallet['address']}
                        =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB ====="""
                        
                        email_text = """\
                            From: %s
                            To: %s
                            Subject: %s

                            %s
                            """ % (sent_from, ", ".join(to), subject, body)

                        try:
                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                            server.ehlo()
                            server.login(gmail_user, gmail_password)
                            server.sendmail(sent_from, to, email_text)
                            server.close()
                        
                            print ('Email sent!')
                        except:
                            print('Something went wrong...')
            else:
                print('\n [' + str(count) + '] ------------------------')
                print('🔁 Total Checked 👇[' + str(total) + '] ')
                print('\nmnemonic_words  : ', mnemonic_words)
                for bad_wallet in data:
                    print('Derivation Path : ', bad_wallet['path'], ' : Bitcoin Address : ', bad_wallet['address'])
                    print('Privatekey WIF  : ', bad_wallet['privatekey'])
            
        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)


        elif event == 'mizogg':
            webbrowser.open_new_tab("https://mizogg.co.uk")
        
        elif event == 'face':
            webbrowser.open_new_tab("https://github.com/Mizogg")

    
    window.Close()
    
main()

