from flask import Flask, render_template
import dns.resolver

app = Flask(__name__)

mail_server_ips = ['x.x.x.x' , 'x.x.x.x', 'x.x.x.x']
dnsbl_servers = [
    "all.s5h.net", "b.barracudacentral.org", "bl.spamcop.net", "blacklist.woody.ch",
    "bogons.cymru.com", "combined.abuse.ch", "db.wpbl.info", "dnsbl-1.uceprotect.net",
    "dnsbl-2.uceprotect.net", "dnsbl-3.uceprotect.net", "dnsbl.dronebl.org",
    "drone.abuse.ch", "duinv.aupads.org", "dul.dnsbl.sorbs.net", "dyna.spamrats.com",
    "http.dnsbl.sorbs.net", "ips.backscatterer.org", "ix.dnsbl.manitu.net", "korea.services.net",
    "misc.dnsbl.sorbs.net", "noptr.spamrats.com", "orvedb.aupads.org", "proxy.bl.gweep.ca",
    "psbl.surriel.com", "relays.bl.gweep.ca", "relays.nether.net", "singular.ttk.pte.hu",
    "smtp.dnsbl.sorbs.net", "socks.dnsbl.sorbs.net", "spam.abuse.ch", "spam.dnsbl.anonmails.de",
    "spam.dnsbl.sorbs.net", "spam.spamrats.com", "spamrbl.imp.ch",
    "spamsources.fabel.dk", "ubl.lashback.com", "ubl.unsubscore.com", "virus.rbl.jp",
    "web.dnsbl.sorbs.net", "wormrbl.imp.ch", "z.mailspike.net", "zombie.dnsbl.sorbs.net"
]
blacklisted = []


def check_blacklist(ip_addresses, dnsbl_servers):
    blacklisted_ips = []
    for ip_address in ip_addresses:
        blacklisted_dnsbls = []
        for dnsbl_server in dnsbl_servers:
            try:
                query = '.'.join(reversed(str(ip_address).split('.'))) + '.' + dnsbl_server
                answers = dns.resolver.resolve(query, 'A')
                if answers:
                    blacklisted_dnsbls.append(dnsbl_server)
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except dns.resolver.Timeout:
                pass
        if blacklisted_dnsbls:
            blacklisted_ips.append({'ip_address': ip_address, 'dnsbls': blacklisted_dnsbls})
    return blacklisted_ips


@app.route('/')
def index():
    global blacklisted
    blacklisted = check_blacklist(mail_server_ips, dnsbl_servers)
    return render_template('index.html', mail_server_ips=mail_server_ips, blacklisted=blacklisted)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
