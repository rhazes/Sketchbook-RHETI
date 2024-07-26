function done(url){
    const form = document.querySelector('form');
    form.action = url;
    form.submit();
}

function handleSubmit(e) {
  // e.preventDefault();
  let shouldReturn = false;
  const form = document.querySelector('form');
  const formData = new FormData(form);
  
  const data = Object.fromEntries(formData.entries());

  let btn = e.submitter.value;
  let currentPrompt = Number(formData.get('currentPromptNumber'))
  
  
  if(btn=='prev') {
    // go to the next prompt
    let prevPrompt = Math.max(0,currentPrompt - 1)
    form.action = "/prevPrompt/" + prevPrompt  
    
    shouldReturn = true;
    
  } else if(btn=='next') {
    // go to the next prompt
    // let maxPrompt = Number(formData.get('maxPromptNumber'))
    // let nextPrompt = Math.min(100,currentPrompt + 1)
    let nextPrompt = currentPrompt + 1
    alert(nextPrompt)
    form.action = "/prompt/"+ nextPrompt;
    
    shouldReturn = true;
  }

  return shouldReturn;
}