
import  math
import  random
import  config

class SensorSimulator:
    def __init__(self, sensor_name, data_rate, trigger_value, trigger_data_rate, amplitude, noise_amp, signal_type, remark) -> None:
        
        # Attributes set by config file
        self.sensor_name = sensor_name
        self.data_rate = float(data_rate)
        self.trigger_value = float(trigger_value)
        self.trigger_data_rate = float(trigger_data_rate)
        self.amplitude = float(amplitude)
        self.noise_amp = float(noise_amp)
        self.signal_type = signal_type
        self.remark = remark
        
        # Attributes used to control signal generation
        self.isStarted = False             # control if signal generation is started or not
        self.last_signal_value = 0          # store the priviously generated signal. it is used to check for trigger    
        self.trigger_data_rate_count = 0    # counts every call and used to compare if the witing time to save the data is reached (trigger_data_rate)
        self.time = -1                     # it is counted as a time. on evey call of it increamnts by one
        
#------------------------------------------------------------------------------------------------------------------------

    def get_sensor_data(self):
        
        self.time += 1
        
        #signal = self.get_sine_wave()
        signal = 0.0
        
        if(self.signal_type == "sine_wave"):
            signal = self.get_sine_wave()
        
        # check if data rate is reached. and if not just return the sensor data and False just to log purpose
        if(not self.check_data_rate()):
            return False, signal
        
        save = self.check_if_signal_shall_be_saved_by_trigger(signal)
        
        # if the call is first time any data must be saved by default
        if(not self.isStarted):
            self.isStarted = True
            save = True
        
        # if the signal is going to be saved then the last_signal_value will be replaced by the new signal
        # for next time
        if(save):
            self.last_signal_value = signal
        
        return save, signal
    

#------------------------------------------------------------------------------------------------------------------------    

    def get_sine_wave(self) -> float:
        
        signal = self.amplitude * math.sin( self.time ) + ( self.noise_amp ) * random.normalvariate( 0, 1.)        
        return signal
        
#------------------------------------------------------------------------------------------------------------------------    

    # counts time and if data rate is reached then sensor generation will be executed
    def check_data_rate(self) -> bool:
        data_rate_is_reached = False
        if(self.time % self.data_rate == 0):
            data_rate_is_reached = True
        
        return data_rate_is_reached

#------------------------------------------------------------------------------------------------------------------------    

    # Check if the trigger is satisfied
    def check_if_signal_shall_be_saved_by_trigger(self, signal) -> bool:
        save = False
        if(self.trigger_value != 0.0):
            
            # every time incriment trigger_data_rate_count by one
            self.trigger_data_rate_count += 1 
            
            # else if there is not data trigger value
            if( abs(self.last_signal_value - signal) >= abs(self.trigger_value) ):
                save = True
                self.trigger_data_rate_count = 0
                
            # else if there is not data trigger value, but the loop reach on trigger_data_rate_count save is ture and
            # reset trigger_data_rate_count to zero
            elif (self.trigger_data_rate_count >= self.trigger_data_rate):
                save = True
                self.trigger_data_rate_count = 0
            
        # else if there is not data trigger value, then save every signal data
        else:
            save = True
        
        return save