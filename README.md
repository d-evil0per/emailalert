<pre>


███████╗███╗   ███╗ █████╗ ██╗██╗      █████╗ ██╗     ███████╗██████╗ ████████╗
██╔════╝████╗ ████║██╔══██╗██║██║     ██╔══██╗██║     ██╔════╝██╔══██╗╚══██╔══╝
█████╗  ██╔████╔██║███████║██║██║     ███████║██║     █████╗  ██████╔╝   ██║   
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██╔══██║██║     ██╔══╝  ██╔══██╗   ██║   
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗██║  ██║███████╗███████╗██║  ██║   ██║   
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   
</pre>
**Voice Alert About the latest email Received, Built using python imaplib & email Library**


# Required Libraries:
- gtts
- json
- imaplib
- email



# Configuration
>You need to Edit **mailconfig.json** file , which contains:
><pre>
	{
	    "mail":
	    {
	        "ORG_EMAIL":"@example.com",
	        "FROM_EMAIL":"abc.123",
	        "FROM_PWD":"password",
	        "SMTP_SERVER":"mail.example.com",
	        "SMTP_PORT":"993"
	    }
}
></pre>

# Run
- **python3 emailalert.py**


>#Feel Free to Contribute.. Thanks 



