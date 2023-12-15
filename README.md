# connect2proxy
## Installing when using Anaconda
```
1) Make sure to first install the following packages through Anaconda: ..
2) Download and unzip the connect2proxy package.
3) In the Anaconda navigator launch the PowerShell Prompt
4) Change directory to the unzipped directory
5) Type the following command: pip install ./connect2proxy-main/
   Depending on your system you may need to change to folder name (connect2proxy-main) to something else.
```

## Installing (for usage)
```
git clone git@github.com:ADCLab/connect2proxy.git
pip3 install connect2proxy/
```

## Installing (for development)
```
git clone git@github.com:ADCLab/remoteDBconnector.git
pip3 install -e connect2proxy/
```

## Error when installing
If you see an error when running the pip there is a good chance you need to upgrade pip3 first
```
pip3 install --upgrade pip
```

## Creating vitual env to test

Create directory 
```
mkdir ~/mytestenv
```

Command to create virtual environment 
```
python3 -m venv ~/mytestenv
```

Active
```
source ~/mytestenv/bin/activate
```
Deactivate
```
deactivate
```
