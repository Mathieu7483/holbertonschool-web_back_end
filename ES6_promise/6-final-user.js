import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.all([userPromise, photoPromise.catch(err => err)])
    .then(results => {
      const photoResult = results[1];
      let photoStatus, photoValue;

      const userResult = {
        status: 'fulfilled',
        value: results[0]
      };

      if (typeof photoResult === 'string' && photoResult.includes('cannot be processed')) {
          photoStatus = 'rejected';
          photoValue = `Error: ${photoResult}`; 
      } else {
          photoStatus = 'fulfilled';
          photoValue = photoResult;
      }
      
      return [
        userResult,
        {
          status: photoStatus,
          value: photoValue
        }
      ];
    })
    .catch(error => {
      console.error('Unexpected error:', error);
      return [];
    });
}
