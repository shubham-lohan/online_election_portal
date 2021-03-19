function SelectRedirect() {
    // ON selection of section this function will work
    //alert( document.getElementById('s1').value);

    switch (document.getElementById('s1').value) {
        case "voter":
            window.location = "{%static 'register_voter'%}";
            break;

        case "candidate":
            window.location = "{%static 'register_candidate'%}";
            break;

        case "party":
            window.location = "{%static 'register_party'%}";
            break;
        case "official":
            window.location = "{%static 'register_official'%}";
            break;

        /// Can be extended to other different selections of SubCategory //////
        default:
            window.location = "{%static 'home'%}"; // if no selection matches then redirected to home page
            break;
    }// end of switch 
}