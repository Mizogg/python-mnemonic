import random, codecs, binascii, bip32utils
from mnemonic import Mnemonic
from rich.console import Console
console = Console()
console.clear()
mylist = []

console.print(" [yellow]------------------Made by Mizogg.co.uk-----------------[/yellow]")
console.print("[yellow]           Starting search... Loading btc.txt[/yellow]")
console.print("[yellow]              Mnemonic Database search...[/yellow]")
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print('[purple]     Loading Bitcoin List . .. . .. . . . [/purple]')
filename ='puzzle.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
        
with open(filename) as file:
    add = file.read().split()
add = set(add)


with open('words.txt', newline='', encoding='utf-8') as fl:
    for line in fl:
        mylist.append(line.strip())
        
console.print('[purple] Total Bitcoin Addresses Loaded and Checking : [/purple]',str (line_count))
console.print("[purple]Starting search... Please Wait [/purple]")
console.print("==========================================================")
divs = int(input(" 📋How Many Derivation Paths m/44'/0'/0'/0/ to m/44'/0'/0'/999/ ✍️ -> "))



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
                'bip32_root_key': bip32_root_key_obj.ExtendedKey(),
                'bip32_extended_private_key': bip32_child_key_obj.ExtendedKey(),
                'path': f"m/44'/0'/0'/0/{child}",
                'address': bip32_child_key_obj.Address(),
                'publickey': binascii.hexlify(bip32_child_key_obj.PublicKey()).decode(),
                'privatekey': bip32_child_key_obj.WalletImportFormat(),
            })

count = 0
total = 0
data = []
wordlenght = ['128','256']          
for i in range(0,len(mylist)):
    wordlist = mylist[i]
    data = []
    count += 1
    total += divs
    mnemo = Mnemonic("english")
    mnemonic_words = wordlist
    seed = mnemo.to_seed(mnemonic_words, passphrase="")
    data_wallet()

    for target_wallet in data:
        address = target_wallet['address']
        if address in add:
            print('\nMatch Found')
            console.print('[green]\nmnemonic_words  : [/green]', mnemonic_words)
            console.print('[purple]Derivation Path : [/purple]', target_wallet['path'], '[green] : Bitcoin Address : [/green]', target_wallet['address'])
            console.print('[green]Privatekey WIF  : [/green]', target_wallet['privatekey'])
            with open("winner.txt", "a") as f:
                f.write(f"""\nMnemonic_words:  {mnemonic_words}
                Derivation Path:  {target_wallet['path']}
                Privatekey WIF:  {target_wallet['privatekey']}
                Public Address Bitcoin:  {target_wallet['address']}
                =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====""")
    else:
        console.print('[red] [' + str(count) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        console.print('[red]\nmnemonic_words  : [/red]', mnemonic_words)
        for bad_wallet in data:
            console.print('[purple]Derivation Path : [/purple]', bad_wallet['path'], '[red] : Bitcoin Address : [/red]', bad_wallet['address'])
            console.print('[red]Privatekey WIF  : [/red]', bad_wallet['privatekey'])