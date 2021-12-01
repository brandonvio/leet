const events = {
  1626906516000: {eventType: 'PlugIn'}, // plugin
  1626906531000: {eventType: 'ChargeStart'}, // charge begins
  1626907101000: {eventType: 'ChargeStop'}, // charge stop
  1626907116000: {eventType: 'PlugOut'} // unplug
}

// readings are cumulative and not necessarily in order
const readings =   {
  1626906606000: {kwh: 1.2},
  1626906966000: {kwh: 7.1},
  1626906726000: {kwh: 2.9},
  1626907086000: {kwh: 10.4},
  1626906546000: {kwh: 0.3},
  1626906666000: {kwh: 2.4},
  1626906846000: {kwh: 4.8},
  1626906906000: {kwh: 5.9},
  1626907026000: {kwh: 8.6},
  1626906786000: {kwh: 4}
}

// implement a function calculateAmountToCharge that takes a session's events, readings, and billingRate as arguments
// this function should tell us how much, in cents, a driver owes for their charge session
// payments are complex, so let's handle this in parts
// first, let's handle the case of a per minute charge
// calculate how much the user owes for the time they spent charging if the billing rate's sessionType is per minute
// HINT - the timestamps are unix timestamps in milliseconds

const billingRate1 = {
  sessionType: 'per minute',
  chargeRateCents: 50,
  freeMinutes: 0
}

const billingRate2 = {
  sessionType: 'per kwh',
  chargeRateCents: 50,
  freeMinutes: 0
}

// cool, but there’s another type of session we need to handle.
// sometimes we have to charge per kwh instead of per minute
// expand the calculateAmountToCharge to function to also handle the sessionType per kwh

// one more complication! // sometimes, we want to offer our drivers a certain number of free minutes at the start of their session // during these minutes, the user won’t be charged, whether we’re charging per minute or per kwh // a number of free minutes can be specified in the billing rate // we’ll have to adjust the calculateAmountToCharge function to take this into account // first, let’s alter our condition for per minute sessions to take into account any free minutes

const billingRate3 = {
  sessionType: 'per minute',
  chargeRateCents: 50,
  freeMinutes: 50,
}

const billingRate4 = {
  sessionType: 'per kwh',
  chargeRateCents: 50,
  freeMinutes: 5,
}

const calculateAmountToCharge = (events, readings, billingRate) => {

  // console.log(billingRate,readings)
  // 50 cents per minute.

  if (billingRate.sessionType === 'per minute'){
    let begin = 0
    let end = 0
    for (const event in events){
      console.log(event)
      console.log(events[event])

      if (events[event].eventType === 'ChargeStart'){
        begin = event
      }

      if (events[event].eventType === 'ChargeStop'){
        end = event
      }

      const totalTime = end - begin
      const result = {
        begin,
        end,
        totalMinutes: (totalTime / 1000) / 60
      }

      if (billingRate.freeMinutes >= result.totalMinutes){
        result.totalCostOfCharge = 0
      }
      else {
        result.totalMinutes = result.totalMinutes - billingRate.freeMinutes
        result.totalCostOfCharge = billingRate1.chargeRateCents * result.totalMinutes
      }

      console.log(result)
    }
  }

  let totalKwh = 0
  if (billingRate.sessionType === 'per kwh'){

    const kwhMinuteRate = .9

    console.log('Charge per kwh')
    for (const reading in readings){
      totalKwh = Math.max(totalKwh, readings[reading].kwh)
      console.log(reading, readings[reading].kwh, totalKwh)
    }
  }


  totalKwh = totalKwh - (billingRate.freeMinutes * khwMinuteRate)
  const totalCostKwh = totalKwh * billingRate.chargeRateCents
  console.log({
    totalCostKwh
  })
}


// calculateAmountToCharge(events, readings, billingRate1)
calculateAmountToCharge(events, readings, billingRate3)
