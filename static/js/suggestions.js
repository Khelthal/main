// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
const etiquetas = document.getElementById('etiquetas');
let linkTag = searchWrapper.querySelector("a");
let webLink;

// if user press any key and release
inputBox.onkeyup = (e)=>{
    let userData = e.target.value; //user enetered data
    let emptyArray = [];
    if(userData){
        icon.onclick = ()=>{
            webLink = `https://www.google.com/search?q=${userData}`;
            linkTag.setAttribute("href", webLink);
            linkTag.click();
        }
        emptyArray = suggestions.filter((data)=>{
            //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            // passing return data inside li tag
            return data = `<li>${data}</li>`;
        });
        if (emptyArray.length) {
            searchWrapper.classList.add("active"); //show autocomplete box
            showSuggestions(emptyArray);
        } else {
            searchWrapper.classList.remove("active"); //hide autocomplete box
        }
        let allList = suggBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            //adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", "select(this)");
        }
    }else{
        searchWrapper.classList.remove("active"); //hide autocomplete box
    }
}

function select(element){
    let selectData = element.textContent;
    let opt = document.createElement('option');
    opt.value = selectData;
    opt.innerHTML = selectData;
    opt.onclick = function () {
      freeSuggestion(this);
    };
    etiquetas.appendChild(opt);
    etiquetas.onchange();
    suggestions.splice(suggestions.indexOf(selectData), 1);
    inputBox.value = "";
    icon.onclick = ()=>{
        webLink = `https://www.google.com/search?q=${selectData}`;
        linkTag.setAttribute("href", webLink);
        linkTag.click();
    }
    searchWrapper.classList.remove("active");
}

function showSuggestions(list){
    let listData;
    listData = list.join('');
    suggBox.innerHTML = listData;
}

function freeSuggestion(opt) {
  suggestions.push(opt.value);
  opt.parentNode.remove(opt);
  etiquetas.onchange();
}
