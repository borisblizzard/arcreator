# hltypes
cdef extern from "<hltypes/hstring.h>" namespace "hltypes":

    cdef cppclass Array[T]

    cdef cppclass String:

        String()
        String(char c)
        String(char c, int times)
        String(char* s)
        String(String& s)
        #String(stdstring& s) #can't get working
        String(char* s, int length)
        String(String& s, int length)
        String(int i)
        String(unsigned int i)
        String(float f)
        String(float f, int precision)
        
        bint split(char delimiter, String& out_left, String& out_right)
        bint split(char* delimiter, String& out_left, String& out_right) 
        bint split(String& delimiter, String& out_left, String& out_right) 
        bint rsplit(char delimiter, String& out_left, String& out_right)
        bint rsplit(char* delimiter, String& out_left, String& out_right)
        bint rsplit(String& delimiter, String& out_left, String& out_right)
        int count(char substr)
        int count(char* substr) 
        int count(String& substr) 
        #Array[String] split(char delimiter, int n, bint remove_empty) 
        #Array[String] split(char* delimiter, int n, bint remove_empty)
        #Array[String] split(String& delimiter, int n, bint remove_empty)
        #Array[String] rsplit(char delimiter, int n, bint remove_empty)
        #Array[String] rsplit(char* delimiter, int n, bint remove_empty)
        #Array[String] rsplit(String& delimiter, int n, bint remove_empty) 
        bint starts_with(char* s) 
        bint starts_with(String& s) 
        bint ends_with(char* s) 
        bint ends_with(String& s) 
        String lower() 
        String upper() 
        String reverse()
        bint is_digit()
        bint is_int() 
        bint is_float(bint require_dot) 
        bint is_number() 
        bint is_hex() 
        String trim(char c) 
        String ltrim(char c) 
        String rtrim(char c) 
        String replace(char* what, char* with_what)
        String replace(String& what, char* with_what)
        String replace(char* what, String& with_what) 
        String replace(String& what, String& with_what)
        String replace(int pos1, int n1, String& str)
        String replace(int pos1, int n1, String& str, int pos2, int n2)
        String replace(int pos1, int n1, char* s)
        String replace(int pos1, int n1, char* s, int n2)
        String replace(int pos1, int n1, char c, int n2)
        bint contains(char c)
        bint contains(char* s) 
        bint contains(String& s)
        int size() 
        int length()

        #operator float() 
        #operator int()
        #operator bint() 

        # operator= not yet suported by cython
        #void operator=(float f)
        #void operator=(int i)
        #void operator=(int i)
        #void operator=(bint b)
        #void operator=(stdstring& s) #can't get working
        #void operator=(char* s)

        # operator+= not yet suported by cython
        #void operator+=(float f)
        #void operator+=(int i)
        #void operator+=(int i)
        #void operator+=(bint b)
        #void operator+=(char c)
        #void operator+=(stdstring& s) #can't get working
        #void operator+=(char* s)

        String operator+(char* s)
        String operator+(char c)
        String operator+(char* s) 
        String operator+(String& s)
        #String operator+(stdstring& s) #can't get working
        bint operator==(float f)
        bint operator==(int i) 
        bint operator==(unsigned int i)
        bint operator==(bint b)
        bint operator==(char* s)
        #bint operator==(stdstring& s) #can't get working
        String operator()(int start, int count) 
        String operator()(int start, int count, int step)
        String operator()(int index)
        char& operator[](int index)
        char& operator[](int index)
        
        char* c_str()

# Alias for simpler code.
#ctypedef String hstr
# Alias for simpler code.
#ctypedef String& chstr


cdef extern from "<hltypes/harray.h>" namespace "hltypes":
    cdef cppclass Array[T]:
        Array()
        Array(Array[T]& other)
        Array(T& elemen)
        Array(T& elemen, int times)
        Array(Array[T]& other, int count)
        Array(Array[T]& other, int start, int count)
        Array(T other[], int count)
        Array(T other[], int start, int count)

        T& operator[](int index)

        Array[T] operator()(int start, int count)
        bint operator==(Array[T]& other)
        bint operator!=(Array[T]& other)

        int size()

        bint equals(Array[T]& other)
        bint nequals(Array[T]& other)

        int index_of(T element)
        
        Array[int] indexes_of(T element)

        bint contains(T& element)
        bint contains(Array[T]& other)
        bint contains(T other[], int count)

        int count(T element)

        void insert_at(int index, T& element, int times)
        void insert_at(int index, Array[T]& other)
        void insert_at(int index, Array[T]& other, int count)
        void insert_at(int index, Array[T]& other, int start, int count)
        void insert_at(int index, T other[], int count)
        void insert_at(int index, T other[], int start, int count)

        T remove_at(int index)
        Array[T] remove_at(int index, int count)

        void remove(T element)
        void remove(Array[T]& other)

        int remove_all(T& element)
        int remove_all( Array[T]& other)

        void push_back(T& element)
        void push_back(T& element, int times)
        void push_back(Array[T]& other)
        void push_back(Array[T]& other, int count)
        void push_back(Array[T]& other, int start, int count)
        void push_back(T other[], int count)
        void push_back(T other[], int start, int count)
        void push_front(T& element, int times)
        void push_front(Array[T]& other)
        void push_front(Array[T]& other, int count)
        void push_front(Array[T]& other, int start, int count)
        void push_front(T other[], int count)
        void push_front(T other[], int start, int count)
        T pop_front()
        Array[T] pop_front(int count)
        T pop_back()
        Array[T] pop_back( int count)
        void unite(T& element)
        void unite(Array[T]& other)
        Array[T] united(T& element)
        Array[T] united(Array[T]& other)
        void intersect(Array[T]& other)
        Array[T] intersected(Array[T]& other)
        void differentiate(T& element)
        void differentiate(Array[T]& other)
        Array[T] differentiated(T& element)
        Array[T] differentiated(Array[T]& other)
        void reverse()
        Array[T] reversed()
        void remove_duplicates()
        Array[T] removed_duplicates()
        void sort()
        void sort(bint (*compare_function)(T, T))
        Array[T] sorted()
        Array[T] sorted(bint (*compare_function)(T, T))
        void randomize()
        Array[T] randomized()
        T min()
        T min(bint (*compare_function)(T, T))
        T max()
        T max(bint (*compare_function)(T, T))
        T random()
        Array[T] random(int count, bint unique)
        
        String join(String& separator)

        Array[T] find_all(bint (*condition_function)(T))
        T* find_first(bint (*condition_function)(T))
        bint matches_any(bint (*condition_function)(T))
        bint matches_all(bint (*condition_function)(T))
        bint includes(T& element)
        bint includes(Array[T]& other) 
        bint includes(T other[], int count)
        bint has(T& element)
        bint has(Array[T]& other) 
        bint has(T other[], int count)
        bint has_element(T& element)
        bint has_element(Array[T]& other)
        bint has_element(T other[], int count)
        void add(T& element)
        void add(T& element, int times)
        void add(Array[T]& other)
        void add(Array[T]& other, int count)
        void add( Array[T]& other, int start, int count)
        void add(T other[], int count)
        void add(T other[], int start, int count)
        void append(T& element)
        void append(T& element, int times)
        void append(Array[T]& other)
        void append(Array[T]& other, int count)
        void append(Array[T]& other, int start, int count)
        void append(T other[], int count)
        void append(T other[], int start, int count)
        void push_last(T& element)
        void push_last(T& element, int times)
        void push_last(Array[T]& other)
        void push_last(Array[T]& other, int count)
        void push_last(Array[T]& other, int start, int count)
        void push_last(T other[], int count)
        void push_last(T other[], int start, int count)
        void push_first(T& element, int times )
        void push_first(Array[T]& other)
        void push_first(Array[T]& other, int count)
        void push_first(Array[T]& other, int start, int count)
        void push_first(T other[], int count)
        void push_first(T other[], int start, int count)
        T pop_first()
        Array[T] pop_first(int count)
        T pop_last()
        Array[T] pop_last(int count)
        T remove_front()
        Array[T] remove_front(int count)
        T remove_back()
        Array[T] remove_back(int count)
        T remove_first()
        Array[T] remove_first(int count)
        T remove_last()
        Array[T] remove_last(int count)
        T pop(int index)
        Array[T] pop(int index, int count)
        T pop_at(int index)
        Array[T] pop_at(int index, int count)
        int pop_all(T& element)
        int pop_all(Array[T]& other)
        Array[T]& operator<<(T& element)
        Array[T]& operator<<(Array[T]& other)

        # operator+= not yet suported by cython
        #Array[T]& operator+=(T& element)
        #Array[T]& operator+=(Array[T]& other)

        # operator-= not yet suported by cython
        #Array[T]& operator-=(T element)
        #Array[T]& operator-=(Array[T]& other)

        # operator|= not yet suported by cython
        # Array[T]& operator|=(T& element)
        # Array[T]& operator|=(Array[T]& other)

        # operator&= not yet suported by cython
        #Array[T]& operator&=(Array[T]& other)

        # operator/= not yet suported by cython
        #Array[T]& operator/=(T& element)
        #Array[T]& operator/=(Array[T]& other)

        Array[T] operator+(T& element) 
        Array[T] operator+(Array[T]& other)
        Array[T] operator-(T element)
        Array[T] operator-(Array[T]& other)
        Array[T] operator|(T& element)
        Array[T] operator|(Array[T]& other)
        Array[T] operator&(Array[T]& other)
        Array[T] operator/(T& element)
        Array[T] operator/(Array[T]& other)

# Alias for simpler code.
#ctypedef Array harray

