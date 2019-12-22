const request = (url, method = 'GET', csfr_token) =>
  fetch(url, {
    method,
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csfr_token
    }
  });

const venueDeleteButton = document.querySelector('#venue-del-btn');
const artistDeleteButton = document.querySelector('#artist-del-btn');

if (venueDeleteButton) {
  venueDeleteButton.addEventListener('click', event => {
    event.preventDefault();
    const { id, token } = event.target.dataset;

    request(`/venues/${event.target.dataset.id}`, 'DELETE', token)
      .then(res => res.json())
      .then(response => {
        window.location.assign('/');
        return response;
      })
      .catch(err => console.log(err));
  });
}

if (artistDeleteButton) {
  artistDeleteButton.addEventListener('click', event => {
    event.preventDefault();
    const { id, token } = event.target.dataset;

    request(`/artists/${event.target.dataset.id}`, 'DELETE', token)
      .then(res => res.json())
      .then(response => {
        window.location.assign('/');
        return response;
      })
      .catch(err => console.log(err));
  });
}
