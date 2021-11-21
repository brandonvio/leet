var delay = (seconds) => new Promise((resolves, rejects) => {

    if (seconds > 10) {
        rejects(new Error(`${seconds} is too long!`))
    }

    setTimeout(() => {
        resolves('the long delay has ended')
    }, seconds * 1000);
});

delay(11)
  .then((msg) => { console.log(msg + " (first then)(no return value)") })
  .then(() => 42)
  .then((number) => console.log(`Hello world: ${number}`))
  .catch((error) => console.log(`error: ${error.message}`));

console.log('end first tick');
