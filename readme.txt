################################################################################################################

namecoinfiles.org On-Chain Image Reconstruction

################################################################################################################

© 2025 by Uwe Martens · www.namecoin.pro · Web3 ID: https://dotbit.app

################################################################################################################

This is a Python script to reconstruct the on-chain images created on the Namecoin blockchain
by namecoinfiles.org (Wayback Archive: https://web.archive.org/web/20140922231746/http://namecoinfiles.org/).

Original GitHub: https://github.com/karelbilek/namecoin-files



INSTRUCTIONS
----------------------------------------------------------------------------------------------------

1. Install Python
-----------------

	Download and install Python from https://www.python.org/downloads/


2. Install dependencies
-----------------------

	Run the following command in the terminal or CMD console to install the required library:

		pip install requests


3. Install Namecoin Core
------------------------

	Download and install Namecoin Core from https://namecoin.pro/SitePages/Software%20Wallets.aspx


4. Configure RPC credentials
----------------------------

	On a fresh installation create (otherwise edit) the file "namecoin.conf" in the Namecoin data directory.
	Minimal content as predefined in this package (replace xxxxxxxxxxxxxxxxxxxxxxxxxxxx with your own credentials):

		server=1
		namehistory=1
		rpcuser=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
		rpcpassword=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
		rpcport=8336
		rpcallowip=127.0.0.1
		rpcbind=127.0.0.1
		nameencoding=hex
		valueencoding=hex
		fallbackfee=0.0002

	Data directory locations:

		Windows:
		_______

			%AppData%\Namecoin


		macOS (enable visibility with 'command chflags nohidden ~/Library' in the terminal before):
		___________________________________________________________________________________________

			~/Library/Application Support/Namecoin/


		Linux:
		______

			$HOME/.namecoin/


5. Start Namecoin Core
----------------------

	Run Namecoin Core in full hex mode with name history enabled.
	You can either define this in namecoin.conf as shown above or start over the CMD console/terminal, e.g. on Windows with:

	C:
	cd C:\Program Files\Namecoin\
	namecoin-qt -server -namehistory -nameencoding=hex -valueencoding=hex

	Alternatively start the minimalistic Namecoin daemon, e.g. on Windows with:

	C:
	cd C:\Program Files\Namecoin\daemon
	namecoind -server -namehistory -nameencoding=hex -valueencoding=hex


6. Create fragments list
------------------------

	Write the fragments’ names in ASCII cleartext line by line into the file "fragments.txt" (as predefined in this package for asset namecoinfiles.org_logo_2.png).


7. Define the file variable
---------------------------

	Set the variable "file" with the asset’s name, e.g.:

		nf/namecoinfiles.org_logo.png
		nf/namecoinfiles.org_logo_2.png
		nf/namecoinfiles.org_logo_100x57.png


8. Run the script
-----------------

	Run the script "reconstruct.py".
	The reconstructed file will be generated in the same folder.
