// cajón de sastre (untranslatable expression)
// common, basic functions on simple types with no specific business logic
// to be splitted in smaller, dedicated files if it grows too much

export function sleep_secs(secs: number) {
    return new Promise(resolve => setTimeout(resolve, secs * 1000));
}