import uploadPhoto from './utils.js';
import createUser from './utils.js';

export default async function asyncUploadUser() {
  const photoPromise = uploadPhoto();
  const userPromise = createUser();

  const [photoResult, userResult] = await Promise.allSettled([photoPromise, userPromise]);
  
  return {
  photo: response_from_uploadPhoto_function,
  user: response_from_createUser_function,
};
{
  photo: null,
  user: null,
}
}
