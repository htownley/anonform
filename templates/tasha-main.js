document.title = "Natasha"

var divnav = document.createElement('div');
divnav.id = 'nav';
document.getElementById('container').appendChild(divnav);

var text = ['FIRST', 'CLICK'];
var id = ['nav-first', 'nav-click'];
var x = document.getElementById('nav');
for (var i in text){
    var button = document.createElement('BUTTON');
    button.id = id[i];
    button.appendChild(document.createTextNode(text[i]));
    x.appendChild(button);
}

for (var i = 1; i < id.length; i++){
    document.getElementById(id[i]).className = "navlink";
}

document.getElementById('nav-first').className = "navlink navactive";


var divMain = document.createElement("div");
divMain.id = 'main';
document.getElementById('container').appendChild(divMain);

var divFirst = document.createElement("div");
divFirst.id = 'main-first';
divFirst.className = 'maindiv mainactive'
document.getElementById('main').appendChild(divFirst);


var divClick = document.createElement("div");
divClick.id = 'main-click';
divClick.className = 'maindiv'
document.getElementById('main').appendChild(divClick);

var selectedNav = document.getElementById('nav-first');
var showMain = document.getElementById('main-first');

var allNavLinks = Array.from(document.getElementsByClassName('navlink'));
for (i=0; i<allNavLinks.length; i++){
    allNavLinks[i] = addEventListener('click', event =>{
        var strname = String(event.target.id);
        var ID = 'main'+strname.substring(3);
        var mDiv = document.getElementById(ID);
        showMain.className = 'maindiv';
        mDiv.className = 'maindiv mainactive';
        showMain = mDiv;
        selectedNav.className = 'navlink';
        mDiv.className = 'navlink navactive';
        selectedNav = window[event.target.id];
    })
}
// $('#main-first').append('<div id="images"></div>');
// $('#images').append('<div id="ImageUpDiv"><p>Upload Image</></div>');
// $('#images').append('<div id="imageUploader"></div>');

$('#main-click').append('<div id="bandContainer"></div>');
$('#bandContainer').append('<div id="bandTitleDiv"><p>Katy Perry</></div>');
$('#bandContainer').append('<div id="concertsDiv"></div>');

$.get("https://rest.bandsintown.com/artists/Katy%20Perry/events?app_id=katy_perry", function(data, status){
    var res = data;
    console.log(status);
    console.log[res];
    var FinalArr = [];
    for (var i=0; i < res.length; i++){
        var venue = res[i]['venue']['name'];
        var city = res[i]['venue']['city'];
        var region = res[i]['venue']['region'];
        var country = res[i]['venue']['country'];
        var dateTime = res[i]['datetime'];
        var str = venue + ', ' + city + ', ' + region + ', ' + country + ': ' + dateTime;

        var eventDiv = document.createElement("div");
        eventDiv.id = 'eventDiv';
        eventDiv.innerText = str; 
        document.getElementById('concertsDiv').appendChild(eventDiv); 
        FinalArr.push(str);
    }
    var ouput = FinalArr.join(' \n ');
    $('#concertsDiv').append('<div id="eventDiv"></div>').text(output);
});
