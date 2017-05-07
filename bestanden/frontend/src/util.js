import { config } from './config.js'

//logs a message, if debug is enabled in config.js
export function log(message) {
    if(config.debug) {
        console.log(message);
    }
}

//checks if an object is defined
export function isset(object) {
    return (typeof object != 'undefined');
}

//capitalises a string
export function title(string) {
    if(string != null) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
}