export default function handleResponseFromAPI(promise) {
  promise
    .then(() => {
      console.log("Got a response from the API");
    })
    .catch(() => {
      console.log("Error getting response from the API");
    });
}
