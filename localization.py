MESSAGES = {
    # Italian
    "it": {
        # start command
        "START_COMMAND": (
            '<b>Ciao</b>, questo bot ti aiuterà a cercare film, libri e altri tipi di media '
            'nel canale @PalestineMovies.\n\n<b>Lista rapida dei comandi:</b>\n'
            '• /cerca - Cerca film, libri e altro disponibili nel canale\n'
            '\n• /iscrivimi - Iscriviti per ricevere aggiornamenti dal canale @PalestineMovies\n'
            '• /disiscrivimi - Annulla l\'iscrizione per non ricevere più aggiornamenti dal canale @PalestineMovies\n'
            '\n• /richiedi - Richiedi un film, un libro o altro\n'
            '• /contatta - Invia un messaggio all\'amministratore\n'
            '\nPer saperne di più su questo progetto e per una spiegazione più dettagliata del funzionamento del bot, '
            'usa il comando /help.'
        ),

        # search command
        "SEARCH_NO_QUERY": "Per favore fornisci cosa vuoi cercare.\n\nEsempio: /search <i>nome del film</i>",
        "SEARCH_SHORT_QUERY": "Spiacente, devi inserire almeno 4 caratteri.",
        "SEARCH_NO_MEDIA_FOUND": "Nessun media trovato.",

        # subscribe and unsubscribe commands
        "SUBSCRIBE_SUCCESS": "Ti sei iscrittə per ricevere nuove uscite dal canale @PalestineMovies.",
        "SUBSCRIBE_ALREADY_SUBSCRIBED": "Sei già iscrittə per ricevere nuove uscite dal canale @PalestineMovies.",
        "UNSUBSCRIBE_SUCCESS": "Ti sei disiscrittə per non ricevere nuove uscite dal canale @PalestineMovies.",
        "UNSUBSCRIBE_NOT_SUBSCRIBED": "Non sei iscrittə per ricevere nuove uscite dal canale @PalestineMovies.",

        # request command
        "REQUEST_EMPTY": (
            "Specifica cosa vuoi richiedere (inserisci anche l'anno di uscita o un link con più "
            "informazioni, se possibile).\n\nEsempio: /richiedi <i>nome del film, anno, link</i>"
        ),
        "REQUEST_SUCCESS": "La tua richiesta è stata ricevuta, grazie per il tuo contributo!",

        # contact command
        "CONTACT_EMPTY": "Per favore fornisci un messaggio da inviare all'amministratore.\n\nEsempio: /contatta <i>il tuo messaggio</i>",
        "CONTACT_SUCCESS": "Il tuo messaggio è stato inviato all'amministratore, ti verrà inviata una risposta a breve (tramite questo bot).",

        # reply command
        "REPLY_EMPTY": "Per favore fornisci un messaggio da inviare all'utente.\n\nEsempio: /rispondi <i>user_id il tuo messaggio</i>",
        "REPLY_HEADER": "📬 <b>Messaggio dall'amministratore:</b>\n\n",
        "REPLY_FOOTER": "\n\n<i>Rispondi a questo messaggio usando nuovamente il comando /contatta.</i>",

        # help command
        "HELP_COMMAND_HEADER": (
            '<b>Cos\'è @PalestineMovies?</b>\n'
            'È un canale che mira ad archiviare tutti i film, libri e altri tipi di media riguardanti '
            'e/o realizzati da persone palestinesi. L\'obiettivo è sensibilizzare sulla causa palestinese '
            'e sul genocidio in corso che Israele sta commettendo, con la complicità dei leader politici occidentali. '
            'L\'arte, la letteratura, e il cinema possono cambiare le menti (auspicabilmente), e mettere tutto questo '
            'insieme in un canale può essere utile e conveniente, e più facile da condividere con parenti e amicз.\n\n'
            '<b>Perché questo bot?</b>\n'
            'Il contenuto del canale sta crescendo, e potrebbe essere più difficile da navigare. Questo bot ti aiuterà a cercare media '
            'e a ricevere aggiornamenti sul progetto. Ti permetterà anche di richiedere un film, un libro o altro, e di inviare '
            'un messaggio all\'amministratore. Può anche essere utile in caso di ban, per restare in contatto con il progetto.\n\n'
            '<b>Lista dei comandi:</b>\n'
            '• /cerca - Cerca film, libri e altro disponibili nel canale.\nEsempio: <code>/cerca nome del film</code>\n'
            '\n• /iscrivimi - Iscriviti per ricevere aggiornamenti sul progetto. In futuro, se necessario, questo diventerà anche un modo '
            'per ricevere nuove uscite come film, libri, ecc...\n'
            '• /disiscrivimi - Annulla l\'iscrizione per non ricevere più aggiornamenti sul progetto.\n'
            '\n• /richiedi - Richiedi un film, un libro o altro. L\'anno di uscita e/o un link con più informazioni sono opzionali ma '
            'molto apprezzati.\nEsempio: <code>/richiedi nome del film, anno, link</code>\n'
            '• /contatta - Invia un messaggio all\'amministratore, per suggerimenti, problemi o altro.\nEsempio: <code>/contatta il tuo messaggio</code>\n'
        ),
        "ADMIN_HELP_COMMAND": (
            '\n<b>Comandi amministratore:</b>\n'
            '• /rispondi - Invia un messaggio ad une utente.\nEsempio: <code>/rispondi user_id il tuo messaggio</code>\n'
            '• /broadcast - Rispondi con questo ad un messaggio per inviarlo a tuttз lз utenti iscrittз.\n'
            '• /stats - Mostra il numero di utenti e di iscrittз.\n'
            '• /view - Mostra l\'album di media costruito.\n'
            '• /broadcast_album - Invia l\'album di media a tuttз lз utenti iscrittз.\n'
            '• /clear - Elimina l\'album di media.\n'
            '• /superbroadcast - Invia un messaggio a tuttз lз utenti.\n'
            '• /riavvia - Riavvia il bot.\n'
        ),
        "HELP_COMMAND_FOOTER": (
            '\nSe vuoi dare un\'occhiata al codice sorgente di questo bot, lo puoi trovare su GitHub: '
            'https://github.com/PalestineArchive/PalestineMoviesBot\n'
            'Sentiti liberə di contribuire al progetto, segnalare bug o suggerire nuove funzionalità.'
        ),
    },

    # English
    "en": {
        # start command
        "START_COMMAND": (
            '<b>Hello</b>, this bot will help you search movies, books, and other types of media '
            'in the @PalestineMovies channel.\n\n<b>Quick list of commands:</b>\n'
            '• /search - Search for movies, books, and other media available in the channel\n'
            '\n• /subscribe - Receive new updates about @PalestineMovies\n'
            '• /unsubscribe - Unsubscribe from receiving new updates about @PalestineMovies\n'
            '\n• /request - Request a movie, book, or whatever\n'
            '• /contact - Send a message to the admin\n'
            '\nTo learn more about this project and for a more detailed explanation of how the bot works, '
            'use the /help command.'
        ),

        # search command
        "SEARCH_NO_QUERY": "Please provide what you want to search.\n\nExample: /search <i>movie name</i>",
        "SEARCH_SHORT_QUERY": "Sorry, you must enter at least 4 characters.",
        "SEARCH_NO_MEDIA_FOUND": "No media found.",

        # subscribe and unsubscribe commands
        "SUBSCRIBE_SUCCESS": "You have been subscribed to receive new media releases from the @PalestineMovies channel.",
        "SUBSCRIBE_ALREADY_SUBSCRIBED": "You are already subscribed to receive new media releases from the @PalestineMovies channel.",
        "UNSUBSCRIBE_SUCCESS": "You have been unsubscribed from receiving new media releases from the @PalestineMovies channel.",
        "UNSUBSCRIBE_NOT_SUBSCRIBED": "You are not subscribed to receive new media releases from the @PalestineMovies channel.",

        # request command
        "REQUEST_EMPTY": (
            "Specify what you want to request (also include the release year and/or a link with more "
            "information, if possible).\n\nExample: /request <i>movie name, year, link</i>"
        ),
        "REQUEST_SUCCESS": "Your request has been received, thank you for your contribution!",
        
        # contact command
        "CONTACT_EMPTY": "Please provide a message to send to the admin.\n\nExample: /contact <i>your message</i>",
        "CONTACT_SUCCESS": "Your message has been sent to the admin, a reply will be sent to you soon (through this bot).",

        # reply command
        "REPLY_EMPTY": "Please provide a message to send to the user.\n\nExample: /reply <i>user_id your message</i>",
        "REPLY_HEADER": "📬 <b>Message from the admin:</b>\n\n",
        "REPLY_FOOTER": "\n\n<i>Reply to this message by using again the /contact command.</i>",

        # help command
        "HELP_COMMAND_HEADER": (
            '<b>What is @PalestineMovies?</b>\n'
            'This is a channel that aims to archive all the movies, books, and other types of media '
            'about and/or made by Palestinian people. The goal is to raise awareness about the Palestinian cause '
            'and the ongoing genocide that Israel is committing, with the complicity of the Western political leaders. '
            'Art, literature, cinematography can change minds (hopefully), and putting those all together in this channel '
            'can be useful and convenient, and easier to share with relatives and friends.\n\n'
            '<b>Why this bot?</b>\n'
            'The channel\'s content is growing, and it becomes difficult to navigate. This bot will help you search for media '
            'and receive new updates about the project. It will also allow you to request a movie, book, or whatever, and to send '
            'a message to the admin. It can also be useful in the event of a ban, to keep in touch with the project.\n\n'
            '<b>Commands list:</b>\n'
            '• /search - Search for movies, books, and other media available in the channel.\nExample: <code>/search movie name</code>\n'
            '\n• /subscribe - Subscribe to receive updates about the project. In the future, if necessary, this will also '
            'become a way to receive new releases like movies, books, etc...\n'
            '• /unsubscribe - Unsubscribe from receiving new updates about the project.\n'
            '\n• /request - Request a movie, book, or whatever. The release year and/or a link with more information are optional but '
            'greatly appreciated.\nExample: <code>/request movie name, year, link</code>\n'
            '• /contact - Send a message to the admin, for suggestions, problems, or anything else.\nExample: <code>/contact your message</code>\n'
        ),
        "ADMIN_HELP_COMMAND": (
            '\n<b>Admin commands:</b>\n'
            '• /reply - Send a message to a user.\nExample: <code>/reply user_id your message</code>\n'
            '• /broadcast - Reply with this to a message to send it to all subscribed users.\n'
            '• /stats - Show the number of users and subscribers.\n'
            '• /view - Show the built media album.\n'
            '• /broadcast_album - Send the media album to all subscribed users.\n'
            '• /clear - Clear the media album.\n'
            '• /superbroadcast - Send a message to all users.\n'
            '• /restart - Restart the bot.\n'
        ),
        "HELP_COMMAND_FOOTER": (
            '\nIf you want to take a look at the source code of this bot, you can find it on GitHub: '
            'https://github.com/PalestineArchive/PalestineMoviesBot\n'
            'Feel free to contribute to the project, report bugs, or suggest new features.' 
        ),
    }
}


def get_localized_message(update, message_key, **kwargs):
    if update in ["it", "en"]:
        language_code = update
    else:
        language_code = update.effective_user.language_code
    try:
        return MESSAGES[language_code][message_key]
    except:
        return MESSAGES['en'][message_key]
