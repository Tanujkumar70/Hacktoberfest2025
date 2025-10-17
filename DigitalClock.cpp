#include <iostream>
#include <chrono>       // For std::chrono::seconds and std::this_thread::sleep_for
#include <thread>       // For std::this_thread
#include <ctime>        // For std::time, std::localtime, and std::strftime
#include <iomanip>      // For stream manipulators (though not strictly needed here)

using namespace std;

void runDigitalClock() {
    // Character buffer to store the formatted time string (e.g., "15:30:45")
    const int buffer_size = 80;
    char buffer[buffer_size];

    // The infinite loop for the clock
    while (true) {
        // 1. Get the current time in seconds since the Epoch
        time_t now = time(0);
        
        // 2. Convert to local time structure
        // Note: localtime is NOT thread-safe, but is okay for simple programs.
        // For production, use localtime_s (Windows) or localtime_r (POSIX).
        tm* ltm = localtime(&now);

        // 3. Format the time into the desired HH:mm:ss string.
        // %H: Hour (00-23), %M: Minute (00-59), %S: Second (00-59)
        strftime(buffer, buffer_size, "%H:%M:%S", ltm);

        // 4. Print the output
        // "\r" (Carriage Return) moves the cursor to the beginning of the line,
        // overwriting the previous output.
        cout << "\rCurrent Time: " << buffer << flush;

        // 5. Wait for 1 second (1000 milliseconds)
        try {
            this_thread::sleep_for(chrono::seconds(1));
        } catch (const exception& e) {
            // In C++, InterruptedException doesn't exist, we just catch generic exceptions
            // or rely on signals for interruption, which is more complex.
            cerr << "Clock sleep interrupted: " << e.what() << endl;
            break; 
        }
    }
}

int main() {
    // Start the clock
    runDigitalClock();
    return 0;
}
