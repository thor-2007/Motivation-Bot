import random
import requests
import schedule
import time
import threading

MOTIVASJONS_QUOTES = [
    "Tro på deg selv. Ingen andre gjør det, men du kan late som.",
    "Hvis du ikke vet hva du driver med – gratulerer, du er voksen.",
    "Livet er ikke et sprintløp, det er mer som en rolig spasertur med stein i skoen.",
    "Start dagen med kaffe og fortrengning. Resten ordner seg kanskje.",
    "Du er unik. Akkurat som alle andre som sa nei til deg på Tinder.",
    "Hvis alt føles håpløst, spis litt brød. Det hjelper ikke, men brød er godt.",
    "Du kan klare alt – bortsett fra matte uten kalkulator.",
    "Gi aldri opp! Bare ta en pause på ubestemt tid.",
    "Du er ikke lat. Du er i horisontal tenkemodus.",
    "Folk sier du kan bli hva du vil. Så hvorfor er du fortsatt trøtt?",
    "Det finnes to typer mennesker: De som får ting gjort, og du.",
    "Hvis livet gir deg sitroner, bygg en katapult og kast dem tilbake.",
    "Selvtillit er å rope 'JA' uten å vite hva spørsmålet var.",
    "Du er den beste versjonen av deg selv. Den trenger bare en oppdatering.",
    "Prøv og feil. Men mest feil, for læringens skyld.",
    "Motivasjon er som deodorant – viktig, men ofte glemt.",
    "Alle snubler iblant. Du bare gjør det med mer dramatikk.",
    "En dårlig dag betyr bare at i morgen kan bli verre. Yay, perspektiv!",
    "Det er aldri for sent å gi opp. Bare ikke gjør det før lunsj.",
    "Du har potensial. Et sted. Vi finner det kanskje.",
    "Gjør ditt beste. Hvis ikke, gjør noe som ser ut som innsats.",
    "Stress ned. Eller stress opp. Det går over uansett, til slutt.",
    "Du er som en muffins: Søt, men kollapser under press.",
    "Målsetting er viktig. Mitt mål i dag? Ikke søle kaffe.",
    "Det er mandag. Kos deg så godt du kan uten å bli sparket.",
    "Hvis du føler deg tom inni, sjekk om du har spist.",
    "Du er stjernestøv med en forkjærlighet for panikk.",
    "Det er ikke en dårlig dag før du velter kaffen – to ganger.",
    "Selvrealisering starter med å stå opp. Der stopper det ofte også.",
    "Ikke vær så hard mot deg selv. Verden tar seg av det.",
    "Du er hovedkarakteren i et drama du ikke forstår plottet i.",
    "Alt går over – bortsett fra meldinger fra banken.",
    "Hvis du ikke vet hva du skal gjøre, gjør det med selvtillit og joggebukse.",
    "Du er som Bluetooth – funker bare når du vil.",
    "Suksess krever innsats. Eller bare flaks og en god unnskyldning.",
    "Ikke sammenlign deg med andre. De har også rot hjemme.",
    "Du er som en PowerPoint-presentasjon: Helt OK, men ingen ser frem til deg.",
    "Motgang former deg. Men kanskje la den slippe litt opp nå?",
    "Du er ikke kaos. Du er... kreativ rot.",
    "Du har overlevd hver dag så langt. Sterk statistikk!",
    "Hvis det ikke funker, prøv igjen. Hvis det fortsatt ikke funker, gi skylda på værmelding.",
    "Du kan være alt du vil. Men først: dusj og spis.",
    "Du har kontroll. Eller i hvert fall illusjonen av det.",
    "Du er ikke glemsk – du er bare tidsreisende uten retning.",
    "Planlegg dagen. Ignorer planen. Gjenta i morgen.",
    "Livet er en simulator uten bruksanvisning.",
    "Du trenger ikke ha alt på stell. Bare lat som for naboene.",
    "Hvis det føles som kaos – det er fordi det er det.",
    "Du er ikke bakpå. Du er bare i reverse med stil.",
    "Husk: En gang var du bare en klump celler. Se på deg nå! En klump med stress!",
    "Hvis alt annet feiler – ta en lur.",
    "Du er som et passord du glemte. Full av potensiale, men låst inne.",
    "La dagen begynne! Eller ligg her og vurder det.",
    "Du er et arbeidsjern! Litt rustent, men fortsatt i bevegelse.",
    "Gjør noe i dag som fremtidige deg kan takke deg for. Eller skylde på.",
    "Du har motivasjon! Den bare sover akkurat nå.",
    "Du er som et internett-abonnement – ustabil og dyr.",
    "Du trenger ikke gjøre alt. Bare noe. Eller ingenting med stolthet.",
    "Alt ordner seg. Kanskje ikke for deg, men for noen.",
    "Hvis du føler deg liten, husk at du tar opp plass på bussen.",
    "Du er et geni! På veldig smale, ubrukelige områder.",
    "Livet er et rot. Bli en del av innredningen.",
    "Du er viktig. Spesielt for algoritmer og reklamefirmaer.",
    "Gi aldri opp – med mindre det er treningsstudio, da kan du gå hjem.",
    "Du har en aura av forvirring og kaffe – det er vakkert.",
    "Hver dag er en mulighet til å gjøre noe... eller bare overleve.",
        "Tro på deg selv – selv speilbildet ditt later som.",
    "Reis deg opp og gå… til kjøleskapet, du fortjener det.",
    "Du er solen i noens dag. Mest fordi du brenner dem ut.",
    "Hver gang du faller, tenk: 'Oi, det var dramatisk!'",
    "Du er ikke lat, du sparer bare energi til apokalypsen.",
    "Du har kontroll over livet ditt. Bare ikke over fjernkontrollen.",
    "Gi alt – unntatt passordet ditt.",
    "Livet er som en sokk uten par: rart og ensomt, men nyttig.",
    "Hvis du ikke vet hva du driver med – perfekt, det gjør ingen.",
    "Vær den endringen du vil se i verden. Eller bare endre senga di.",
    "Du er verdifull. Minst som en brukt pose fra Rema.",
    "Når det stormer, vær paraplyen som blåser vekk først.",
    "Start dagen som en sjef: forvirret og med kaffe.",
    "Ikke tenk for mye – det gir deg bare idéer.",
    "Du er ikke rotete, du er en estetisk katastrofe.",
    "Husk at selv en potet kan bli chips.",
    "Du er unik – akkurat som 8 milliarder andre.",
    "Drøm stort. Sov lenge.",
    "Din motivasjon er som internett i 1999 – treg og ustabil.",
    "Du er dagens helg – alle ser frem til deg, men ingen jobber for deg.",
    "Dersom du ikke har noe å si, si det høyt og med selvtillit.",
    "Du er som en mikrofon: Alle roper på deg når du ikke virker.",
    "Ta livet med en klype salt – og gjerne sjokolade.",
    "Du er et kreativt kaos. Mest kaos.",
    "Du kan ikke feile hvis du aldri prøver. Inspirerende, ikke sant?",
    "Livet er en dans på Lego.",
    "Hvis planen din ikke funker, kall det for ‘forskning’.",
    "Du er som en ballong i motvind – ingen kontroll, men festlig å se på.",
    "Folk flest er rare. Du bare mer enn gjennomsnittet.",
    "Du har potensial. Det er bare ute og handler.",
    "Noen dager er som sokker i sandaler – ukomfortable og rare.",
    "Du er ikke bakpå. Du bare løper baklengs.",
    "Vær en stjerne – eksploder dramatisk og lys opp alle andres liv.",
    "Når du ikke vet hva du gjør, smil. Det funker på møter.",
    "Du er som en vits uten punchline – folk ler likevel.",
    "Ikke vær best. Vær underholdende.",
    "Selvtillit er å trykke 'send' uten å lese meldingen på nytt.",
    "Du er som en TV uten signal – mystisk og litt støyete.",
    "Du er den beste versjonen av deg selv. Beta 0.1.",
    "Husk: Ikke alle helter dusjer.",
    "Gjør noe meningsfylt i dag. Som å late som du trener.",
    "Du er ikke treig, du er bare i tide til neste uke.",
    "Hvis livet er et teater, er du backstage og forvirret.",
    "Du har ett talent: Å være til stede og forvirret.",
    "Snu motgang til motbakkeløp – i crocs.",
    "Du er ikke glemt – bare midlertidig arkivert.",
    "Du er en walking reminder om at alt går an med kaffe.",
    "Ikke vær deg selv – vær en bedre versjon av nabokatta.",
    "Husk: Hver dag er en ny sjanse til å spise snacks i stedet for å rydde.",
    "Du er ikke svak. Du er bare på lavt batteri.",
    "Livet er et eventyr. Mest som sidekarakteren med dårlig flaks.",
    "Du er som en god ide klokka 03:00 – upraktisk, men engasjerende.",
    "Hvis du ikke vet hvor du skal, ta en lur og vurder senere.",
    "Du er dagens overraskelse. Ingen vet hva du gjør her.",
    "Du er ikke et problem. Du er et uplanlagt prosjekt.",
    "Noen har talenter. Du har... entusiasme?",
    "Vær modig! Eller se veldig bestemt ut mens du later som.",
    "Hvis alt annet feiler, bli plante.",
    "Du er limet i gruppa. Tørket, men fortsatt der.",
    "Du er en legende – i egne notater.",
    "Du er som en romrakett: Høytflyvende og lett antennelig.",
    "Gjør i dag bedre enn i går. Eller bare bytt klær.",
    "Du er viktig. Du holder stolen i ro når du sitter.",
    "Vær den kaffen du ønsker å se i verden.",
    "Du er i balanse – mellom kaos og panikk.",
    "Livet gir deg muligheter. Du gir dem videre.",
    "Du er ikke ferdig. Du er 'work in regression'.",
    "Du er en livsform med adgang til internett og muffins.",
    "Hvis du føler deg tom, er det plass til mer kake.",
    "Du har styrke – mest i tommelen fra scrolling.",
    "Du er ikke rot. Du er et konsept uten plan.",
    "Når alt feiler, bare si: 'Det var et valg.'",
    "Du er et mirakel med sokker som ikke matcher.",
    "Hvis du føler deg ubrukelig, husk at du har vært WiFi-hotspot én gang.",
    "Selv potetmos begynte som noe hardt.",
    "Du er ikke treg – du er en sen versjon av fremtiden.",
    "Du er kreativ. Bare veldig inkonsekvent.",
    "Verden trenger deg. Eller i hvert fall noen gjør det. Kanskje.",
    "Du er som en onsdag – ingen vet helt hva de skal med deg.",
    "Du er et gående ‘før’-bilde.",
    "Når alt er kaos – dans! Ingen vet hva du prøver på uansett.",
    "Du er ikke tapt. Du er på omvei med stil.",
    "Du har selvtillit – det bare venter bak latskapen.",
    "Hvis livet er hardt, legg det i bløt.",
    "Du er dagens meme – morsom, men litt tragisk.",
    "Du er som et forlatt Word-dokument – åpent, men tomt.",
    "Vær deg selv. Eller lat som, det er nærme nok.",
    "Du har én jobb. Og du... prøver.",
    "Du er en blanding av entusiasme og ‘meh’.",
    "Du er som en potteplante – trenger lys, vann og ro.",
    "Vær solen i rommet – forstyrrende og varm.",
    "Du er bevis på at 'bra nok' faktisk er nok.",
    "Du har kraft – mest i stemmen når pizzaen er forsinket.",
    "Livet er kort. Spis frokost til middag.",
    "Du er ikke ubrukelig – du er overkvalifisert til å slappe av.",
    "Du er som caps lock – plutselig, intens og ofte feil brukt.",
    "Du er oppdatert! Med bugs og alt.",
    "Du er et ikon. På skrivebordet. Ubrukt siden 2019.",
    "Glem ikke: Du er elsket. Mest av algoritmer.",
    "Du er energien til en katt i solskinn – lat og lykkelig.",
    "Du er magisk. Spesielt god til å forsvinne fra ansvar.",
    "Selv drager tar pauser. Du er som en trøtt firfisle – og det er greit.",
    "Vær som teip – ikke nødvendigvis sterk, men alltid der.",
    "Du er som et nyvasket kjøleskap – sjelden, men imponerende.",
    "Du er dagens vibe: Litt forvirra, men med stil.",
    "Du er en ukjent superhelt – Kaptein For Sent.",
    "Du er ikke alene. Du har stemmen i hodet og tre apper åpne.",
    "Når noen sier 'du klarer det', bare nikk og løp.",
    "Du er som et pledd – trøstende og alltid i sofaen.",
    "Gi aldri opp! Med mindre det regner og du har Netflix.",
    "Du er midtpunktet i en rolig storm av distraksjon.",
        "Ikke stress, ingen vet hva de driver med uansett – vi bare later som med bedre klær.",
    "Livet handler ikke om hvor fort du går, men hvor mye snacks du får med på veien.",
    "Selv solen trenger en pause bak skyene – og du trenger fem.",
    "Du er ikke på villspor, du er på sightseeing i livet.",
    "Gi 110 %. Eller bare 11 % med god holdning.",
    "Du er som et kaffefilter – du slipper igjennom det viktigste og svir resten.",
    "Gjør én ting i dag. Eller lat som. Det er nesten det samme.",
    "Du har motivasjon! Den bare tok en litt for lang lunsjpause.",
    "Dersom dagen er grå, legg til farger med høylytte sukk og rare sokker.",
    "Alt ordner seg. Eller det går over, og så glemmer vi det.",
    "Du er som en pizzaboks – firkantet, flatt og fullt av gode greier.",
    "Når du føler deg tom, husk at du kan fylles med vafler.",
    "Ingen har livet på stell – noen har bare ryddet forsiden.",
    "Du er et mysterium. Som en IKEA-manual uten skruer.",
    "Stå opp, strekk deg og husk: ingen vet at du ikke gjør noe.",
    "Livet går opp og ned – litt som WiFi-en din.",
    "Du er ikke sen – du er bare ekstra grundig med oppvarmingen.",
    "Du er som en app: Veldig nyttig når du virker.",
    "Hvis livet var et spill, ville du være NPC-en med de beste replikker.",
    "Du er som en lyspære – av og på, men lyser av og til opp rommet.",
    "Gjør det for deg selv. Eller for å ha noe å si i morgen.",
    "Du er en brainstorm med regnvær og glitter.",
    "Du er ikke rotete, du er et konsept i utvikling.",
    "Når motivasjonen svikter, klem en pute og lat som det var en idé.",
    "Du har uante evner – spesielt evnen til å ignorere ansvar.",
    "Du er som en sudoku – ingen forstår deg, men folk prøver.",
    "Hvis du ikke kan vinne, bli en dommer i eget liv.",
    "Du er ikke lat, du er bare mentalt parkert.",
    "Livet er en quiz uten svaralternativer. Du gjetter nydelig.",
    "Du er proof of concept på at kaffe og vilje holder en dag sammen.",
    "Du er ikke ubrukelig – du er bare på pause fra stordåd.",
    "Hvis du ikke kan motivere deg selv, motivér noen andre og stjel energien.",
    "Du er som en plastpose i vinden – uforutsigbar og litt poetisk.",
    "Husk: Du er en gave. Uten kvittering.",
    "Du kan klare alt! Bortsett fra å forstå NAV-skjemaer.",
    "Du er som en USB-C-lader – nesten ingen vet hvor du passer, men du er viktig.",
    "Du er stjernen i en film du ikke skjønner sjangeren til.",
    "Du er ikke treig – du er bare i sirupmodus.",
    "Om du ikke lykkes, bruk stemmen til Siri og prøv igjen.",
    "Du er en legende i ditt eget Google-søk.",
    "Hvis ting går skeis, skyld på vær eller gravitasjon.",
    "Du er som en koselig feil – rar, men verdsatt.",
    "Du er dagen i dag sin største underholder.",
    "Du er ikke forvirret – du bare utforsker alle muligheter samtidig.",
    "Du er som en rosin i kjeksen – overraskende og diskutabel.",
    "Du er WiFi-signalet i noens liv. Litt ustabil, men helt nødvendig.",
    "Du er som et kart over T-banen: Full av stopp og fortsatt fremover.",
    "Om livet gir deg brokkoli, stek det og lat som det er snacks.",
    "Du er ikke bakpå, du kjører bare i eco-mode.",
    "Du er verdens beste til å være deg – uslåelig rekord!",
    "Du er en blanding av brødrister og brannfare – spennende og litt farlig.",
    "Hver dag du ikke gir opp, vinner du mot dyna.",
    "Du er som en fisk på land – malplassert, men nysgjerrig.",
    "Du er ikke svak – du er energisparende.",
    "Motivasjon er som et ekorn: Plutselig, energisk og borte på 2 sekunder.",
    "Du er en PowerPoint med for mange animasjoner – intens, men minneverdig.",
    "Dersom du ikke vet hva du gjør, gjør det høyt og med gestikulering.",
    "Du er ikke sen – du er bare tidsartistisk.",
    "Du er den typen folk nevner i podcaster uten å si navn.",
    "Du har karakter – spesielt når kaffen er tom.",
    "Du er en kaffe uten sukker – bitter, men effektiv.",
    "Du er stjernestøv med kvittering på stress.",
    "Du er en banan i livets fruktsalat – alltid litt for moden.",
    "Livet er en reklamepause og du er midt i showet.",
    "Du er ikke feil, du er spesialversjonen uten instruksjoner.",
    "Du er dagens vinner i 'beste uplanlagte øyeblikk'.",
    "Du er en ny idé midt i en gammel plan.",
    "Du er viktig – som ketchup i en bagett.",
    "Du er ikke ute å kjøre – du ruller bare sidelengs med stil.",
    "Ingen vet helt hva du driver med – det er det som gjør det spennende.",
    "Du er som sjokolademelk i voksenlivet – uventet, men trengs.",
    "Du er kapteinen på skipet 'Vi får se hvordan det går'.",
    "Du er som en lommelykt uten batteri – irriterende, men fortsatt der.",
    "Du er det lille ekstra i ‘meh’ til ‘tja’.",
    "Du er dagens påminnelse om at rare er bra.",
    "Du er som en uåpnet e-post – mystisk og lett oversett.",
    "Du er som en giraff i et møterom – høy, klumsete og uforberedt.",
    "Du er en lørdag i et mandagskostyme.",
    "Du er tanken som aldri ble skrevet ned – fri og uorganisert.",
    "Du er ikke senil – bare fremovertenkende med dårlig minne.",
    "Du er som et TV-spill på easy – fortsatt utfordrende.",
    "Du er regn i solskinn – ingen vet hvorfor du skjer, men du skjer.",
    "Du er dagens tilfeldige kaos med sjarm.",
    "Du er en blinkende notifikasjon i noens liv.",
    "Du er ikke tom – du er minimalistisk.",
    "Du er som en blyant uten viskelær – ingen tar feil bedre enn deg.",
    "Du er viktig! Akkurat som pappesker – uunnværlig og alltid i veien.",
    "Du er limet i limbo – ingen vet hvor du hører hjemme.",
    "Du er som strømbrudd midt i film – dramatisk og forstyrrende.",
    "Du er det rare smilet i en gruppechat – forvirrende, men hyggelig.",
    "Du er som en YouTube-anbefaling – ingen vet hvorfor du dukket opp, men du blir sett.",
    "Du er ikke et valg – du er et uhell med stil.",
    "Du er som en varmeovn i juli – ulogisk, men helhjertet.",
    "Du er en idé som burde blitt vurdert lenger, men ble gjennomført.",
    "Du er et mesterverk i feil retning.",
    "Du er som en gangbru under bygging – upraktisk, men interessant.",
    "Du er et ekko av entusiasme – litt forsinket, men ekte.",
    "Du er den ekstra ketchup-pakka i en fancy middag.",
    "Du er verdens beste i å være på stedet hvil med uttrykk i ansiktet.",
    "Du er en remix av motivasjon og tilfeldigheter.",
    "Du er en tolkning av 'nesten ferdig'.",
    "Du er som å våkne fra en lur: forvirret, sulten og ikke sikker på hvilken dag det er.",
    "Du er viktig. Ikke akkurat nå, men sånn generelt. Tror vi.",
]


bot_token = input("Skriv inn din Telegram bot token: ")
chat_id = input("Skriv inn Telegram chat ID for å sende meldinger: ")


# --- Funksjoner ---
def hent_teit_quote():
    return random.choice(MOTIVASJONS_QUOTES)

def send_quote():
    quote = hent_teit_quote()
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": quote}
    try:
        requests.post(url, data=payload)
        print(f"✅ Sendte melding: {quote}")
    except Exception as e:
        print(f"❌ Feil ved sending: {e}")

# --- Planlagt kjøring ---
paused = False
running = True

def run_schedule():
    while running:
        if not paused:
            schedule.run_pending()
        time.sleep(1)

# --- Oppsett ---
print("Velg når du vil motta meldinger:")
print("1 – Send nå")
print("2 – Hver X minutter")
print("3 – Hver X timer")
print("4 – Hver dag på spesifikt klokkeslett (HH:MM, 24-timers)")

valg = input("Ditt valg (1/2/3/4): ")

if valg == "1":
    send_quote()

elif valg == "2":
    antall_min = input("Hvor mange minutter mellom hver melding? ")
    try:
        antall_min = int(antall_min)
        schedule.every(antall_min).minutes.do(send_quote)
    except:
        print("⚠️ Ugyldig tall. Avslutter.")
        exit()

elif valg == "3":
    antall_timer = input("Hvor mange timer mellom hver melding? ")
    try:
        antall_timer = int(antall_timer)
        schedule.every(antall_timer).hours.do(send_quote)
    except:
        print("⚠️ Ugyldig tall. Avslutter.")
        exit()

elif valg == "4":
    klokkeslett = input("Skriv klokkeslett i 24-timers format (f.eks. 08:00 eller 23:45): ")
    try:
        time.strptime(klokkeslett, "%H:%M")
        schedule.every().day.at(klokkeslett).do(send_quote)
    except:
        print("⚠️ Ugyldig klokkeslett.")
        exit()
else:
    print("⚠️ Ugyldig valg.")
    exit()

# --- Start tråd for planlagte meldinger ---
thread = threading.Thread(target=run_schedule)
thread.start()

# --- Kontrollmeny ---
print("\nSkriv 'send' for å sende melding nå")
print("Skriv 'pause' for å stoppe midlertidig")
print("Skriv 'start' for å fortsette")
print("Skriv 'avslutt' for å avslutte\n")

while True:
    kommando = input(">>> ").strip().lower()
    
    if kommando == "send":
        send_quote()
    elif kommando == "pause":
        paused = True
        print("⏸ Pause aktivert.")
    elif kommando == "start":
        paused = False
        print("▶️ Meldinger gjenopptatt.")
    elif kommando == "avslutt":
        running = False
        print("🛑 Bot avsluttes...")
        break
    else:
        print("❓ Ukjent kommando. Prøv 'send', 'pause', 'start' eller 'avslutt'.")

