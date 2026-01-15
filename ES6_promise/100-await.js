import uploadPhoto from './utils.js';
import createUser from './utils.js';

export default async function asyncUploadUser() {
  const photoPromise = uploadPhoto();
  const userPromise = createUser();
  const results = await Promise.allSettled([photoPromise, userPromise]);
  
  const response = {
    photo: null,
    user: null,
  };
  results.forEach((result) => {
    if (result.status === 'fulfilled') {
      if (result.value && result.value.id && result.value.name) {
        response.user = result.value;
      } else {
        response.photo = result.value;
      }
    } else {
      if (result.reason && result.reason instanceof Error) {
        if (result.reason.message.includes('Photo')) {
          response.photo = { error: result.reason.message };
        } else if (result.reason.message.includes('User')) {
          response.user = { error: result.reason.message };
        }
      }
    }
  });
  
  return response;
}
