import { login } from './login';
import { protect } from './protected';
import { health } from '../services/health';


export const init = (app) => {
  app.post('/login', login);
  app.get('/protected', protect);
  app.get('/_health', health);
};
